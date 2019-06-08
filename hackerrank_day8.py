# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_input_data(input_data_size):
    data_dict = {}
    for _ in range(input_data_size):
        data = str(input().strip())
        data_split = data.split(' ')
        #print(data_split)
        data_dict.update({data_split[0]:data_split[1]})
    return data_dict

if __name__ == '__main__':
    input_data_size = int(input().strip())
    data_dict = get_input_data(input_data_size)

    for _ in range(input_data_size):
        name = str(input().strip())
        if name in data_dict:
            print("%s=%s" % (name,data_dict[name]))
        else:
            print('Not found')

