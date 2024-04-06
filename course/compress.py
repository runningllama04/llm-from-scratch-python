import gzip

def compress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as f_in:
        with gzip.open(output_filename, 'wb') as f_out:
            f_out.writelines(f_in)

input_filename = 'model-01.pkl'
output_filename = 'model-01.pkl.gz'

compress_file(input_filename, output_filename)