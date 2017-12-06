# Copywrite James Draper 2017.

"Utilites for notebook_mapper."

import sys
import os
import re
import subprocess
import pandas as pd


def native_cmd(cmd, whitespace=False):
    """Returns the output of a native command on a give system.

    NOTE: Results may contain white space charaters at end of lines.
    """
    result = subprocess.check_output(cmd, shell=True).decode()
    if whitespace:
        return result
    else:
        # Remove carrige returns.
        result = re.sub('\r|\n', '', result, re.X)
        return result


def net_use():
    """Return a the results of 'net use' as a pandas DataFrame.
    """
    # Call Windows commandline.
    result = native_cmd('net use', whitespace=True)
    result = re.sub('\r','', result, re.X)

    result = list(filter(lambda x: len(x) > 0, result.split('\n')))[1:-1]
    result = list(filter(lambda x: x[0].isalpha(), result))
    res = [i.split()[:3] for i in result]
    res0 = [' '.join(i.split()[3:]) for i in result]
    res_df = pd.concat([pd.DataFrame(res), pd.DataFrame(res0)], axis=1)
    new_header = res_df.iloc[0]
    res_df = res_df[1:]
    res_df.columns = new_header
    res_df.reset_index(inplace=True, drop=True)
    return res_df


def find_mapped_drive_letter(network_path):
    """Return the drive letter for a connected server.
    """
    # Test if any drives mapped.
    if net_use().shape[0]:

        mask = net_use().Remote.str.contains(network_path)
        result = net_use().loc[mask].Local
        # Connect exists.
        if result.shape == (1,):
            return result[0]
        # FIXME: Connections exist but none containing network_path.
        if result.shape == (0,):
            print('Could not connect.')
            return None
        # In the case of ambiguity the first match is chosen.
        else:
            print('Several drives conatain this phrase:',
                  network_path,
                  "Using:\n",
                  net_use().loc[mask])
            return result[0]
    else:
        print('No mapped drives found.')
        return None


def append_mapped(path, server):
    """Temporarily append a directory on a mapped drive to sys.path

    NOTE: User must have read+write access to the mapped drive for any modules
    to be importable.

    Parameters:
    -----------
    path : str
        The target path WITHOUT the drive letter ex:

            M:\Pics\kittens,

            MUST be in the form;

            Pics\kittens

    server: str
        The target server where path exists. If this string is found
        in the mapped drives then that drive is selected. If several
        drives conatin the same string then the first is selected.

    """

    target_path = os.path.sep.join([find_mapped_drive_letter(server), path])

    if os.path.isdir(target_path):
        sys.path.append(target_path)
        print('Connected to:',
              server,
              ', the following directory has been temporarily appended to system path;',
              target_path)
    else:
        print('Failed to append:', target_path, 'to system path.')