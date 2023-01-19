# Sofia Staley 261035363
# Comp 202 Assignment 3


def is_valid_image(image):
    '''(list<int>) --> bool
    Takes a nested list that represents an image and returns whether
    or not the input gives a valid image.
    
    >>> is_valid_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    
    >>> is_valid_image([[0], [0, 0]])
    False
    
    >>> is_valid_image([["0x5", "200x2"], ["111x7"]])
    False
    '''
    
    element_length = len(image[0])
    
    for element in image:
        for thing in element:
            if type(thing) != int:
                return False
            
            if 255 <= thing <= 0:
                return False
        
        if len(element) != element_length:
            return False
        
        
    return True



def is_valid_compressed_image(image):
    '''(list<>) --> bool
    Checks whether the given image matrix is in valid compressed pgm image format

    >>> is_valid_compressed_image([["0x5", "200x2"], ["111x7"]])
    True
    
    >>> is_valid_compressed_image([[0], [0, 0]])
    False
    
    >>> is_valid_compressed_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    False
    '''
    
    last_B_value = -1
    
    for element in image:
        current_B_value = 0
        
        for thing in element:
            if type(thing) != str:
                return False
            
            if thing.count('x') != 1:
                return False
            
            if not thing[thing.find('x') + 1 :].isdecimal() or '.' in thing or not thing[:thing.find('x')].isdecimal():
                return False
            
            
            if int(thing[:thing.find('x')]) < 0 or int(thing[:thing.find('x')]) > 255:
                return False


            current_B_value += int(thing[thing.find('x') + 1 :])
            
        if last_B_value == -1 or last_B_value == current_B_value:
            last_B_value = current_B_value
        
        else:
            return False
        
    return True



def load_regular_image(filename):
    '''(str) --> list<list<int>>
    Takes a image file name as a string and returns the image matrix contained in the file.
    
    >>> load_regular_image('comp.pgm')
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0],
    [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0],
    [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0],
    [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0],
    [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> load_regular_image('comp.pgm.compressed')
    Traceback (most recent call last):
    AssertionError: Please input a valid file!
    
    >>> load_regular_image('test.pgm')
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    '''
    
    fobj = open(filename, 'r')
    image_matrix = []
    line_counter = 0
    
    for line in fobj:
        if line_counter > 2:
            new_line = line.split()
            sublist = []
            
            for thing in new_line:
                sublist.append(int(thing))
            
            image_matrix.append(sublist)
            
        line_counter += 1
       
       
    fobj.close()
    
    if not is_valid_image(image_matrix):
        raise AssertionError('Please input a valid file!')
    
    return(image_matrix)
    
    
    
def load_compressed_image(filename):
    '''(str) --> list<list<str>>
    Loads a compressed pgm file and writes it as a matrix for the program to use.
    
    >>> load_compressed_image('comp.pgm.compressed')
    [['0x24'],
    ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'],
    ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> load_compressed_image('comp.pgm')
    Traceback (most recent call last):
    AssertionError: Please input a valid file!
    
    >>> load_compressed_image('test.pgm.compressed')
    [['0x5', '200x2'], ['111x7']]
    '''
    
    fobj = open(filename, 'r')
    image_matrix = []
    line_counter = 0
    
    for line in fobj:
        if line_counter > 2:
            new_line = line.split()
            sublist = []
            
            for thing in new_line:
                sublist.append(thing)
            
            image_matrix.append(sublist)
            
        line_counter += 1
        
        
    fobj.close()
    
    if not is_valid_compressed_image(image_matrix):
        raise AssertionError('Please input a valid file!')
    
    return(image_matrix)



def load_image(filename):
    '''(str) --> list<list>
    Loads an image as a matrix for the program to use. Takes into account the file type.
    
    >>> load_image('comp.pgm')
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0],
    [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0],
    [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0],
    [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0],
    [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> load_image('comp.pgm.compressed')
    [['0x24'],
    ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'],
    ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> load_image('comp.pgm') == load_image('comp.pgm.compressed')
    False
    '''
    
    fobj = open(filename, 'r')
    first_line = fobj.read()
    fobj.close()
    
    if 'P2C' in first_line:
        return(load_compressed_image(filename))
        
    elif 'P2' in first_line:
        return(load_regular_image(filename))
        
    else:
        raise AssertionError('Please input a valid file!')
    
    
    
def save_regular_image(image_matrix, filename):
    '''(list<list<int>>, str) --> NoneType
    Takes a compressed image matrix and saves it as a file.
    
    >>> image = [[0]*10, [255]*10, [0]*10]
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> image2 = load_image("test.pgm")
    >>> image2 == image
    True
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    <built-in method read of _io.TextIOWrapper object at 0x106d298a0>
    >>> fobj.close
    
    >>> image = load_image('dragon.pgm')
    >>> save_image(image, 'dragontoo.pgm')
    >>> image == load_image('dragontoo.pgm')
    True
    '''
    
    if not is_valid_image(image_matrix):
        raise AssertionError('Please input a valid file!')
    
    fobj = open(filename, 'w')
    fobj.write('P2\n')
    fobj.write(str(len(image_matrix[0])) + ' ' + str(len(image_matrix)) + '\n')
    fobj.write('255\n')
    
    for line in image_matrix:
        current_line = ''
        for element in line:
            current_line += (str(element) + ' ')
            
        fobj.write(str(current_line[:len(current_line) - 1]) + '\n')
    
    
    fobj.close()   



def get_compressed_width(image_matrix):
    '''(list<list>) --> str
    helper function to get the width of a compressed image from the image matrix assuming the matrix is valid
    
    >>> get_compressed_width([["0x5", "200x2"], ["111x7"]])
    '7'
    
    >>> get_compressed_width([["0x1", '225x3'], ['100x3', '0x1']])
    '4'
    
    >>> get_compressed_width([['0x100'],['100x50', '225x50']])
    '100'
    '''
    width = 0
    
    for line in image_matrix[0]:
        width += int(line[line.find('x') + 1:])
        
    return(str(width))
   


def save_compressed_image(image_matrix, filename):
    '''(list<list<str>>, str) --> NoneType
    Takes a nested list and a filename string and saves an image in compressed pgm format.
    
    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_compressed_image([[0]*10, [255]*10, [0]*10], 'bung.pgm')
    Traceback (most recent call last):
    AssertionError: Please input a valid file!
    
    >>> image = load_image('dragon.pgm')
    >>> save_compressed_image(image, 'dragontoo.pgm')
    Traceback (most recent call last):
    AssertionError: Please input a valid file!
    '''
    
    if not is_valid_compressed_image(image_matrix):
        raise AssertionError('Please input a valid file!')
    
    fobj = open(filename, 'w')
    fobj.write('P2C\n')
    fobj.write(get_compressed_width(image_matrix) + ' ' + str(len(image_matrix)) + '\n')
    fobj.write('255\n')
    
    for line in image_matrix:
        current_line = ''
        for element in line:
            current_line += (element + ' ')
            
        fobj.write(current_line[:len(current_line) - 1] + '\n')
    
    
    
def save_image(image_matrix, filename):
    '''(list<list<>>) --> NoneType
    Saves the given image matrix based on the image type given.
    
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\n7 2\n255\n0x5 200x2\n111x7\n'
    >>> fobj.close()
    
    >>> save_image([[0]*10, [255]*10, [0]*10], 'bung.pgm')
    >>> load_image('bung.pgm')
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> save_image([['0x10'],['0x20']], 'invalid.pgm')
    Traceback (most recent call last):
    AssertionError: Please input a valid file!
    '''
    
    if is_valid_image(image_matrix):
        save_regular_image(image_matrix, filename)
        
    elif is_valid_compressed_image(image_matrix):
        save_compressed_image(image_matrix, filename)
        
    else:
        raise AssertionError('Please input a valid file!')



def invert(image_matrix):
    '''(list<list<int>>) --> list<list<int>>
    Takes a standard image matrix and returns a matrix with inverted color values.
    
    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    
    >>> invert([[225, 225, 225], [77, 150, 33]])
    [[30, 30, 30], [178, 105, 222]]
    
    >>> image = load_image('dragon.pgm')
    >>> image != invert(image)
    True
    '''
    
    if not is_valid_image(image_matrix):
        raise AssertionError('Please input a valid file!')
    
    new_matrix = []
    
    for line in image_matrix:
        new_line = []
        
        for element in line:
            new_line.append(255 - element)
            
        new_matrix.append(new_line)
        
    return(new_matrix)
            
            
            
def flip_horizontal(image_matrix):
    '''(list<list<int>>) --> list<list<int>>
    Takes a standard image matrix and flips it horizontally.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    
    >>> flip_horizontal([[5, 5, 5, 6, 6, 6], [6, 6, 6, 5, 5, 5]])
    [[6, 6, 6, 5, 5, 5], [5, 5, 5, 6, 6, 6]]
    
    >>> image = load_image('comp.pgm.compressed')
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: Please input a valid file!
    '''
    
    if not is_valid_image(image_matrix):
        raise AssertionError('Please input a valid file!')
    
    new_matrix = []
    
    for line in image_matrix:
        new_line = []
        
        for element in line:
            new_line.insert(0, element)
            
        new_matrix.append(new_line)
        
    return(new_matrix)



def flip_vertical(image_matrix):
    '''(list<list<int>>) --> list<list<int>>
    Takes a standard image matrix and flips it vertically. 
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    
    >>> flip_vertical([[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]])
    [[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
    
    >>> image = load_image('comp.pgm.compressed')
    >>> flip_vertical(image)
    Traceback (most recent call last):
    AssertionError: Please input a valid file!
    '''
    
    if not is_valid_image(image_matrix):
        raise AssertionError('Please input a valid file!')
    
    new_matrix = []
    
    for line in image_matrix:
        new_matrix.insert(0, line)
        
    return(new_matrix)



def crop(image_matrix, TLrow, TLcolumn, height, width):
    '''(list<list<int>>) --> list<list<int>>
    Takes a standard image matrix and crops the image given the inputs of where to start the crop, and
    the dimensions of the final cropped image.
    
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]], 1, 2, 2, 1)
    [[6], [10]]
    
    >>> crop([[0,0,0,0,0,0,0,0,0,0],[225,225,225,225,225,225,225,225,225,225],[0,0,0,0,0,0,0,0,0,0]], 1, 0, 2, 9)
    [[225, 225, 225, 225, 225, 225, 225, 225, 225], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> file = load_image('dragon.pgm')
    >>> new_file = crop(file, 0, 0, 200, 200)
    >>> file == new_file
    False
    '''
    
    current_row = 0
    lines_written = 0
    new_matrix = []
    
    
    for line in image_matrix:
        if current_row < TLrow:
            current_row += 1
            continue
           
        if lines_written <= height:
            new_matrix.append(line[TLcolumn : TLcolumn + width])
            lines_written += 1
            
        else:
            break
        
    return(new_matrix)



def find_end_of_repetition(image_line, index, target):
    '''(list<int>, int, int) --> int
    Takes a list of numbers, a starting index, and a target number. Returns the index of
    the last occurance of the target number, assuming the target number is also at the starting index.
    
    >>> find_end_of_repetition([5, 3, 5, 5, 5, -1, 0], 2, 5)
    4
    
    >>> find_end_of_repetition([4, 4, 4, 6 , 4, 4, 4], 3, 6)
    3
    
    >>> find_end_of_repetition([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3], 10, 3)
    10
    '''
    
    index_count = index
    
    for element in image_line[index:]:
        if element != target:
            return(index_count - 1)
        
        else:
            if index_count == (len(image_line) - 1):
                return(index_count)
            
            index_count += 1
    


def compress(image_matrix):
    '''(list<list<int>>) --> list<list<str>>
    Takes a regular image matrix and changes it into a compressed image matrix.
    
    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    
    >>> file_1 = load_image('comp.pgm.compressed')
    >>> file_2 = load_image('comp.pgm')
    >>> file_1 == compress(file_2)
    True
    
    >>> file = load_image('comp.pgm.compressed')
    >>> compress(file)
    Traceback (most recent call last):
    AssertionError: Please input a valid file!
    '''
    
    if not is_valid_image(image_matrix):
        raise AssertionError('Please input a valid file!')
    
    new_matrix = []
    line_counter = 0
        
    while line_counter < len(image_matrix):
        index = 0
        new_line = []
            
        while index < len(image_matrix[line_counter]):
            element = image_matrix[line_counter][index]
            new_index = find_end_of_repetition(image_matrix[line_counter], index, element)
            new_line.append(str(element) + 'x' + str(new_index - index + 1))
             
            index = new_index
            
            if new_index == index:
                index += 1

            
        new_matrix.append(new_line)
        line_counter += 1
        
    return(new_matrix)
                        


def decompress(image_matrix):
    '''(list<list<str>>) --> list<list<int>>
    Takes a compressed image matrix and turns it into a regular image matrix.
    
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    
    >>> file_1 = load_image('comp.pgm')
    >>> file_2 = load_image('comp.pgm.compressed')
    >>> file_1 == decompress(file_2)
    True
    
    >>> decompress([['100x5'], ['3x3', '7x3']])
    Traceback (most recent call last):
    AssertionError: Please input a valid file!
    '''
    
    if not is_valid_compressed_image(image_matrix):
        raise AssertionError('Please input a valid file!')
    
    new_matrix = []
    
    for line in image_matrix:
        new_line = []
        
        for element in line:
            multiple_count = int(element[element.find('x') + 1:])
            multiple = 0
            
            while multiple < multiple_count:
                new_line.append(int(element[:element.find('x')]))
                multiple += 1
                
        new_matrix.append(new_line)
        
    return(new_matrix)



def process_command(command_string):
    '''(str) --> NoneType
    Takes a string of inputs and manipulates the image as given. Will always save and load the final image.
    
    >>> process_command("LOAD<comp.pgm> CP SAVE<comp.pgm.compressed>")
    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'],
    ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
     '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
     '187x1', '0x1', '255x4', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
     '187x1', '0x1', '255x1', '0x4'],
    ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1',
     '255x1', '0x4'],
    ['0x24']]
    
    >>> process_command("LOAD<test.pgm> CR<1,0,2,9> SAVE<testcrop.pgm>>")
    >>> load_image("testcrop.pgm")
    [[255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> process_command('LOAD<mountain.pgm> INV FH FV SAVE<wonkymountain.pgm>>')
    >>> image_1 = load_image('mountain.pgm')
    >>> image_2 = load_image('wonkymountain.pgm')
    >>> image_1 != image_2
    True
    '''
    
    command_list = command_string.split(' ')
    image_matrix = []
    load_filename = ''
    save_filename = ''
    
    for command in command_list:
        if 'LOAD' in command:
            load_filename = command[command.find('<') + 1 : command.find('>')]
            image_matrix = load_image(load_filename)
            
        elif command == 'INV':
            image_matrix = invert(image_matrix)
            
        elif command == 'FH':
            image_matrix = flip_horizontal(image_matrix)
            
        elif command == 'FV':
            image_matrix = flip_vertical(image_matrix)
            
        elif 'CR' in command:
            coords = command[command.find('<') + 1:command.find('>')]
            coords = coords.split(',')
            image_matrix = crop(image_matrix, int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))
            
        elif command == 'CP':
            image_matrix = compress(image_matrix)
            
        elif command == 'DC':
            image_matrix = decompress(image_matrix)
            
        elif 'SAVE' in command:
            save_filename = command[command.find('<') + 1 : command.find('>')]
            save_image(image_matrix, save_filename)
            
        else:
            raise AssertionError('Please input all valid commands!')
        
          

    

    
    
