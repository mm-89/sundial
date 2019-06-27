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

    verify_param2 = False 

    if( verify_param ):
        verify_param2 = True
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
        var_alpha_dim = cp.check_angles_dimension(alpha)
        if ( not var_alpha_dim ):
            verify = False
            print('ATTENTION! ALPHA value is not the right dimension!')
            verify_param2 = False
        var_beta_dim = cp.check_angles_dimension(beta)
        if ( not var_beta_dim ):
             verify = False
             print('ATTENTION! BETA value is not the right dimension!')
             verify_param2 = False
        var_lamb_dim = cp.check_angles_dimension(lamb)
        if ( not var_lamb_dim ):
            verify = False
            print('ATTENTION! LAMBDA value is not the right dimension!')
            verify_param2 = False
        var_gamma_dim = cp.check_angles_dimension(gamma)
        if ( not var_gamma_dim ):
            verify = False
            print('ATTENTION! GAMMA value is not the right dimension!')
            verify_param2 = False

        if( verify_param2 ):
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
        
        verify_param3 = False
        if( verify_param2 ):
            verify_param3 = True
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
            var_monlist_dim = cp.check_monlist_dimension(mon_to_plot)
            if ( not var_monlist_dim ):
                print('ATTENTION! MONTHS value is not the right dimension!')
                verify_param2 = False
            var_daylist_dim = cp.check_daylist_dimension(day_to_plot)
            if ( not var_daylist_dim ):
                print('ATTENTION! DAY value is not the right dimension!')
                verify_param2 = False
            var_monlist_typ = cp.check_mon_list_type(mon_to_plot)
            if ( not var_monlist_typ ):
                print('ATTENTION! MONTHS value are wrong!')
                verify_param2 = False
            var_daylist_typ = cp.check_day_list_type(day_to_plot)
            if ( not var_daylist_typ ):
                print('ATTENTION! DAY value are wrong!')
                verify_param2 = False

        if( verify_param3 ):
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

        

    return lon_to_read, lat_to_read,\
            alpha_to_read, beta_to_read,\
            lamb_to_read, gamma_to_read, \
            mon_to_read, day_to_read


