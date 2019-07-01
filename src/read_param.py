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
    print('Select value for LAT is: %s' % lat)
    print('Select value for LON is:  %s' % lon)
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

    print('...')
    print(' ')
 
    if( verify_param ):
        
        print('Generating LAT and LON needed to the model ...')
        print(' ')
        lon_to_read = cp.trans_degree_decimal_lon(lon)
        lat_to_read = cp.trans_degree_decimal_lat(lat)
        print(' ')
        print('Finish to generate such variables')
        print(' ')
        print('*******************************************')
        print(' ')
    
    
    else:
        print('Program stopped')
        print('')

    if( verify_param ):
        print('*******************************************')
        print(' ')
        print('Initializing to check ALPHA BETA LAMBDA and GAMMA value')
        print(' ')
        print('*******************************************')
        print(' ')
        print('Select value for ALPHA is: %s' % alpha)
        print('Select value for BETA is:  %s' % beta)
        print('Select value for LAMBDA is: %s' % lamb)
        print('Select value for GAMMA is:  %s' % gamma)
        print(' ')
        print('Verify ALPHA BETA LAMBDA and GAMMA .........')
        print(' ')
        print('...')

        print(' ')
        print('Generating ALPHA BETA LAMBDA and GAMMA needed to the model ...')
        print(' ')

        alpha_to_read = cp.trans_degree_to_radiant(float(alpha))
        beta_to_read = cp.trans_degree_to_radiant(float(beta))
        lamb_to_read = cp.trans_degree_to_radiant(float(lamb))
        gamma_to_read = cp.trans_degree_to_radiant(float(gamma))

        print('Finish to generate such variables')
        print(' ')
        print('*******************************************')
        print(' ')

    else:
        print('Program stopped')
        print('')
        
    if( verify_param ):
        print('*******************************************')
        print(' ')
        print('Initializing to check MONTHS and DAYS value')
        print(' ')
        print('*******************************************')
        print(' ')
        print('Select value for MONTHS is: %s' % mon_to_plot)
        print('Select value for DAYS is:  %s' % day_to_plot)
        print(' ')
        print('Verify MONTHS and DAYS value .........')
        print(' ')
        print('...')
        print(' ')
        print(' ')
        print('Generating MONTH and DAY lists needed to the model ...')
        print(' ')
          
        mon_to_read = cp.transform_month(mon_to_plot)
        day_to_read = cp.transform_days(day_to_plot)

        print('Finish to generate such variables')
        print(' ')
        print('*******************************************')
        print(' ')

    else:
        print(' ')
        print('Program stopped')
        print('')

    if( verify_param ):
        print('*******************************************')
        print(' ')
        print('Initializing to check UTC value')
        print(' ')
        print('*******************************************')
        print(' ')
        print('Select value for MONTHS is: %s' % UTC)
        print(' ')
        print('...')
        print(' ')
        utc_to_read = cp.transform_UTC(UTC)

    return lon_to_read, lat_to_read,\
            alpha_to_read, beta_to_read,\
            lamb_to_read, gamma_to_read, \
            mon_to_read, day_to_read, \
            utc_to_read


