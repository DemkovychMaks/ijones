import ijones
import reader
import writer

if __name__ == '__main__':
    data = reader.read_plate_file("ex_1.txt")
    result = ijones.IJones(*data)
    print(result)
    writer.write_file("ijones.out.txt", result)

