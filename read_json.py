#!/bin/python
#coding=utf8

import simplejson as json
import sys


#to generate query and tag
def main(args):
    line_result = ""
#decode json
    f = file(args[1])
    query_file = args[2]
    write_file = args[3]
    source = f.read()
    
    json_object = json.JSONDecoder().decode(source)
    
    
#read query_file
    with open(write_file, 'w') as result_file:
        with open(query_file,'r') as wordbag:
            for line in wordbag:
                line_list = line.strip().decode("utf8").split(' ')
                line_result = ''
                
                #whether all
                
                if json_object["criteria"]["custom"]["pv_all"] == True:
                    line_result += "全量#".decode("utf8")    
             
                #traverse origin
                origin_length = len(json_object["criteria"]["origin"])
            
                for pos_idx in range(origin_length):
                    csv_pos_idx = json_object["criteria"]["origin"][pos_idx]["csv_pos_idx"]
                    tag = line_list[int(csv_pos_idx)]
                    col_option = json_object["criteria"]["origin"][pos_idx]["csv_col_option"]
                    
                    if tag in col_option: #json_object["criteria"]["origin"][pos_idx]["csv_col_option"]
    
                        line_result += tag +"#"
            
                
                #traverse combined
                
                combined_length = len(json_object["criteria"]["combined"])
                
                for combined_idx in range(combined_length):
                    option_name = json_object["criteria"]["combined"][combined_idx]["csv_option_name"]
                    options_length = len(json_object["criteria"]["combined"][combined_idx]["csv_col_options"])
                    
                    for pos_idx in range(options_length):
                        idx_key = json_object["criteria"]["combined"][combined_idx]["csv_col_options"][pos_idx]["csv_pos_idx"] 
                        col_option_name = json_object["criteria"]["combined"][combined_idx]["csv_col_options"][pos_idx]["csv_col_option"]
                        
                        judge = 1
                        if line_list[idx_key] == col_option_name:
                            judge = judge * 1
                        else:
                            judge = judge * 0
                            break
    
                    if judge != 0:
                        line_result += option_name + "#"


                if line_result != "":
                    line_result = line_list[0] + '\t' + line_result
                    result_file.write(line_result[:-1].encode("utf8"))
                    result_file.write("\n")

if __name__ == "__main__":
    main(sys.argv)
