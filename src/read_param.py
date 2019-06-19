import sys

sys.path.insert(0, '../')

from namelist import *
import check_param as cp

### PROGRAM ################################

def program_check():

    verify_param = True

    print('*******************************************')
    print(' ')
    print('Initializing to check LON and LAT value')
    print(' ')
    print('*******************************************')
    print(' ')
    print('Select value for LAT is: ', lat)
    print('Select value for LON is:  ', lon)
    print(' ')
    print('Verify LAT and LON .........')
    print(' ')
    print('...')
    print(' ')

    var1 = cp.check_type_and_len_coordinates_lon(lon)
    var2 = cp.check_type_and_len_coordinates_lat(lat)

    if(var1 == True and var2 == True):
        print('LAT and LON are correct type and lenght')
    elif(var1 == True and var2 == False):
        verify_param = False
        print('ATTENTION! LAT value is not the right type or lenght!')
    elif(var1 == False and var2 == True):
        verify_param = False
        print('ATTENTION! LON value is not the right type or lenght!')
    elif(var1 == False and var2 == False):
        verify_param = False
        print('ATTENTION! LAT and LON value are not the right type or lenght!')

    var3 = cp.check_dimension_coordinates_lon(lon)
    var4 = cp.check_dimension_coordinates_lat(lat)
    
    print(' ')
    print('...')
    print(' ')

    if(var3 == True and var4 == True):
        verify_param = False
        print('LAT and LON are correct dimension')
    elif(var3 == True and var4 == False):
        verify_param = False
        print('ATTENTION! LAT value is not the right dimension!')
    elif(var3 == False and var4 == True):
        verify_param = False
        print('ATTENTION! LON value is not the right dimension!')
    elif(var3 == False and var4 == False):
        verify_param = False
        print('ATTENTION! LAT and LON value are not the right dimension!')
    
    print(' ')
    print('*******************************************')
    print(' ')
    
    # HERE PUT OTHER TESTS
    
    if( verify_param ):
        
        print('Generating the set of variable needed to the model ...')
        print(' ')
        lon_to_read = cp.trans_degree_decimal_lon(lon)
        lat_to_read = cp.trans_degree_decimal_lat(lat)
        print(' ')
        print('Finish to generate variable')
        print(' ')
        print('*******************************************')
    
    
    else:
        print('Program stopped')
        print('')
    
    return


