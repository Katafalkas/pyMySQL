#!/usr/bin/env python

import subprocess

def parameter_value(status, parameter):
        """
        Function that will return a MySQL "show slave status" or "show master status" specified parameter
        INPUT: status = 'master' or 'slave'; parameter = 'Seconds_Behind_Master' or 'Position' or any other name of parameter from "show slave status" or "show master status"
        OUTPUT: a value of parameter you have named in INPUT
        EXAMPLE :       If you want to know MySQL binlog position from "SHOW MASTER STATUS;", enter:
                                parameter_value('master', 'Position')
                        which will return a value of binlog potition:
                                958745
                        Or if you want to know the seconds behind master from "SHOW SLAVE STATUS \G", enter:
                                parameter_value('slave', 'Seconds_Behind_Master')
                        which will return current replication delay from masterin seconds:
                                125
        """
        status = subprocess.Popen(['mysql', '-e', 'show %s status \G' % status], shell=False, stdout=subprocess.PIPE)
        output_status_full  = status.communicate()
        output_status_str = output_status_full[0]
        output_status_list = output_status_str.splitlines()
        output_status_list = output_status_list[1:]
        output_status_list_of_pairs = []
        for i in output_status_list:
                output_status_list_of_pairs.append(i.split(':'))
        output_status_list_of_pairs_clean = []
        for i in output_status_list_of_pairs:
                output_status_list_of_pairs_clean.extend([i[0].replace(' ', ''), i[1]])

        output_status_dict = dict(zip(output_status_list_of_pairs_clean[0::2], output_status_list_of_pairs_clean[1::2]))
        return output_status_dict[parameter]

def main():
        print parameter_value('master', 'Position')


if __name__ == '__main__':
        main()

