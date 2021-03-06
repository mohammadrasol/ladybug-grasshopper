# Ladybug: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Ladybug.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Deconstruct a Ladybug Header into its components.
-

    Args:
        _header: The header of the DataCollection (containing metadata).
    Returns:
        location_: Location data as a ladybug Location or location string
            (Default: unknown).
        data_type: Type of data (e.g. Temperature) (Default: unknown).
        unit: Units of the data_type (e.g. C) (Default: unknown)
        a_period: A Ladybug AnalysisPeriod object.
"""

ghenv.Component.Name = "LadybugPlus_Deconstruct Header"
ghenv.Component.NickName = 'XHeader'
ghenv.Component.Message = 'VER 0.0.04\nOCT_14_2018'
ghenv.Component.Category = "LadybugPlus"
ghenv.Component.SubCategory = '01 :: Analyze Weather Data'
ghenv.Component.AdditionalHelpFromDocStrings = "0"


if _header and hasattr(_header, 'isHeader'):
    location = _header.location
    data_type = _header.data_type
    unit = _header.unit
    a_period = _header.analysis_period