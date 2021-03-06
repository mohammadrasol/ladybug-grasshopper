# Ladybug: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Ladybug.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


"""
Automatically download a .zip file from a URL where climate data resides,
unzip the file, and open .epw, .stat, and ddy weather files.
-

    Args:
        _weather_URL: Text representing the URL at which the climate data resides. 
            To open the a map interface for all publicly availabe climate data (epwmap),
            use the "EPWmap" component.
        _folder_: An optional  file path to a working directory on your computer
            where you would like to download and unzip the file.  If nothing is set,
            the weather files will be downloaded to C:/ladybug/ and placed in a
            folder with the name of the weather file location.
    Returns:
        epw_file: The file path of the downloaded epw file.
        stat_file: The file path of the downloaded stat file.
        ddy_file: The file path of the downloaded ddy file.
"""

ghenv.Component.Name = "LadybugPlus_Download Weather"
ghenv.Component.NickName = 'downloadWeather'
ghenv.Component.Message = 'VER 0.0.04\nOCT_14_2018'
ghenv.Component.Category = "LadybugPlus"
ghenv.Component.SubCategory = '00 :: Ladybug'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

import os
try:
    from ladybug.dotnet import download_file
    from ladybug.futil import unzip_file
except ImportError as e:
    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))

if _weather_URL is not None:
    # name for the weather files
    if _weather_URL.lower().endswith('.zip'):
        # onebuilding URL type
        _folder_name = _weather_URL.split('/')[-1][:-4]
    else:
        # dept of energy URL type
        _folder_name = _weather_URL.split('/')[-2]
    
    # create default working_dir
    if _folder_ is None:
        _folder_ = os.path.join(os.environ['USERPROFILE'], 'ladybug', _folder_name)
    try:
        _folder_.decode('ascii')
    except UnicodeDecodeError:
        raise UnicodeDecodeError('\nYour USERNAME contains a non-ASCII character, meaning files are downloaded to: \n {}'
            '\nUse the _folder_ input to this component to download EPW files to a valid location.'.format(_folder_))
    else:
        print 'Files will be downloaded to: {}'.format(_folder_)
    
    
    # default file names
    epw = os.path.join(_folder_, _folder_name + '.epw')
    stat = os.path.join(_folder_, _folder_name + '.stat')
    ddy = os.path.join(_folder_, _folder_name + '.ddy')
    
    # download and unzip the files if they do not exist
    if not os.path.isfile(epw) or not os.path.isfile(stat) or not os.path.isfile(ddy):
        zip_file_path = os.path.join(_folder_, _folder_name + '.zip')
        download_file(_weather_URL, zip_file_path, True)
        unzip_file(zip_file_path)
    
    # set output
    epw_file, stat_file, ddy_file = epw, stat, ddy