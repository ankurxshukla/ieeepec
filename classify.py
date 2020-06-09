import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
from sklearn.preprocessing import LabelEncoder
import os
os.environ['KERAS_BACKEND'] = 'theano'
import keras

sw = set(stopwords.words('english'))

def remove_sw(text, sw):
    return [w for w in text if w not in sw]

def my_tokenizer(document):
    tokenizer = RegexpTokenizer('[a-zA-Z]+')
    words = tokenizer.tokenize(document.lower())
    words = remove_sw(words, sw)
    ps = SnowballStemmer('english')
    for i in range(len(words)):
        words[i] = ps.stem(words[i])
    return words

model = keras.models.load_model('/ieeepec.h5')
model.load_weights('./ieeepec_weights.h5')
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

vocab = {'manage': 1225, 'activity': 107, 'of': 1388, 'an': 170, 'assembly': 224, 'line': 1188, 'high': 970, 'accuracy': 92, 'optical': 1414, 'components': 466, 'continuous': 512, 'team': 2031, 'oriented': 1431, 'operation': 1406, 'transitioned': 2111, 'new': 1361, 'process': 1559, 'into': 1085, 'production': 1571, 'achieving': 98, '35': 39, '45': 47, 'increase': 1027, 'in': 1020, 'throughput': 2079, 'capability': 353, 'decreased': 589, '10': 1, '30': 35, 'equipment': 755, 'malfunctions': 1223, 'by': 333, 'improving': 1019, 'specifications': 1910, 'and': 180, 'work': 2251, 'procedures': 1558, 'delivered': 596, '15': 12, '20': 18, 'training': 2106, 'teaching': 2030, 'teams': 2033, 'taylor': 2028, 'characteristics': 383, 'based': 271, 'on': 1399, 'customer': 568, 'requirements': 1720, 'ensured': 741, 'compliance': 463, 'with': 2248, 'maximum': 1254, 'efficiency': 707, 'quality': 1629, 'safety': 1774, 'health': 963, 'regulations': 1688, 'trained': 2105, 'operators': 1410, 'technicians': 2036, 'improved': 1016, 'yield': 2274, 'reliability': 1696, 'control': 520, '25': 29, 'currently': 565, 'execute': 775, 'project': 1588, 'contract': 514, 'assignments': 234, 'conduct': 489, 'reviews': 1749, 'for': 864, 'clients': 414, 'specialty': 1907, 'chemicals': 392, 'hazardous': 959, 'waste': 2217, 'petrochemicals': 1491, 'flavor': 853, 'fragrance': 887, 'industries': 1035, 'championed': 377, 'development': 629, 'view': 2202, 'to': 2086, 'increasing': 1029, 'output': 1439, 'reducing': 1675, 'raw': 1652, 'material': 1248, 'usage': 2167, 'environmental': 749, 'impact': 1008, 'commissioned': 444, 'validated': 2178, 'batch': 273, 'size': 1877, 'introduced': 1087, 'cleaning': 410, 'which': 2236, 'reduced': 1674, 'change': 378, 'over': 1443, 'time': 2081, 'solvent': 1897, 'use': 2168, 'purification': 1618, 'step': 1941, 'resolve': 1725, 'concerns': 484, 'then': 2067, 'built': 330, 'this': 2074, 'improve': 1015, 'yields': 2275, 'designed': 613, 'executed': 776, 'plant': 1509, 'test': 2055, 'confirm': 495, 'the': 2064, 'economic': 699, 'operating': 1405, 'feasibility': 822, 'recovering': 1668, 'product': 1570, 'from': 891, 'mother': 1329, 'liquor': 1192, 'savings': 1789, 'potential': 1526, 'implemented': 1013, 'technologically': 2039, 'economically': 700, 'attractive': 248, 'site': 1872, 'treatment': 2115, 'streams': 1956, 'constructed': 505, 'procedure': 1557, 'dsc': 688, '7000': 60, 'that': 2063, 'helped': 969, 'explain': 793, 'different': 642, 'effects': 706, 'various': 2185, 'anti': 191, 'oxidants': 1450, 'plastic': 1510, 'abs': 80, 'injection': 1045, 'molded': 1316, 'chips': 395, 'formulated': 877, 'technique': 2037, 'retrieval': 1741, 'pellets': 1474, 'resulting': 1737, 'cost': 541, '100k': 3, 'investigated': 1094, 'persisting': 1486, 'problems': 1556, 'using': 2173, 'aspen': 220, 'explorer': 795, 'addition': 113, 'catalyst': 363, 'charge': 387, 'during': 691, 'emulsion': 723, 'productivity': 1572, 'month': 1324, 'participated': 1458, 'collaboratively': 433, 'working': 2254, 'mega': 1266, 'extruder': 802, 'upwards': 2163, '500lbs': 51, 'produced': 1567, 'energy': 731, 'balance': 268, 'acrylonitrile': 102, 'staging': 1922, 'tank': 2020, 'identifying': 1000, 'where': 2234, 'was': 2216, 'lost': 1202, 'inefficiency': 1037, 'chemical': 391, 'marketed': 1243, 'proposed': 1596, 'engineered': 733, 'industrial': 1034, 'projects': 1591, 'throughout': 2078, 'southern': 1903, 'california': 344, 'self': 1821, 'starting': 1930, 'dynamic': 693, 'multi': 1336, 'tasking': 2025, 'sole': 1891, 'proprietor': 1599, 'completed': 458, 'oil': 1395, 'field': 831, 'three': 2076, 'phase': 1493, 'water': 2219, 'gas': 909, 'separator': 1832, 'design': 612, 'build': 326, 'within': 2249, 'schedule': 1793, 'saved': 1787, 'client': 413, '250m': 30, 'overall': 1444, 'costs': 542, 'supervised': 1984, 'construction': 506, 'crude': 558, 'storage': 1946, 'farm': 816, 'revamp': 1744, 'under': 2137, 'agreed': 142, 'upon': 2158, 'budget': 323, '125m': 8, 'demonstrated': 601, 'involvement': 1101, 'saving': 1788, 'decisions': 586, 'innovative': 1050, 'expenditure': 784, 'techniques': 2038, 'depth': 609, 'knowledge': 1139, 'hands': 952, 'experience': 786, 'formulation': 878, 'inks': 1048, 'coatings': 424, 'emulsions': 724, 'rheology': 1755, 'characterization': 384, 'assisted': 237, 'company': 453, 'set': 1844, 'up': 2153, 'vietnam': 2201, '1999': 17, 'more': 1327, 'than': 2062, 'us': 2164, 'million': 1296, 'sales': 1776, 'per': 1478, 'year': 2271, 'revised': 1751, 'dozen': 676, 'previous': 1545, 'ink': 1047, 'formulas': 876, 'their': 2065, 'printing': 1552, 'performance': 1481, 'reduce': 1673, 'four': 886, 'such': 1979, 'as': 217, 'electrical': 712, 'circuit': 402, 'boards': 301, 'oversaw': 1446, 'oversight': 1447, 'at': 243, 'commissioning': 445, 'activities': 106, 'developed': 627, 'wrote': 2266, 'start': 1928, 'plans': 1508, 'power': 1527, 'retrofit': 1742, 'procured': 1565, 'valves': 2182, 'items': 1115, 'maintained': 1215, 'engineering': 734, 'spreadsheets': 1916, 'visited': 2206, 'support': 1993, 'observe': 1380, 'progress': 1587, 'ids': 1001, 'worked': 2252, 'other': 1433, 'engineers': 735, 'fix': 849, 'any': 192, 'occur': 1383, 'performed': 1482, 'ensuring': 742, 'licensed': 1180, 'facilities': 808, 'complied': 464, 'federal': 826, 'managed': 1226, 'completion': 461, 'licensing': 1182, 'review': 1747, 'international': 1082, 'isotopes': 1111, 'deconversion': 588, 'facility': 809, 'application': 195, 'successfully': 1978, 'organized': 1430, 'planned': 1506, 'fuel': 893, 'cycle': 571, 'information': 1039, 'exchange': 773, 'attended': 246, '200': 19, 'stakeholders': 1924, '2011': 23, 'through': 2077, '2014': 26, 'played': 1512, 'leading': 1162, 'role': 1762, 'creation': 550, 'page': 1454, 'interim': 1079, 'staff': 1921, 'guidance': 947, 'first': 844, 'medical': 1262, 'united': 2148, 'states': 1934, 'task': 2024, 'capturing': 357, 'lessons': 1172, 'learned': 1164, 'organization': 1427, 'efforts': 710, 'mistakes': 1301, 'future': 905, 'enhanced': 737, 'offered': 1390, 'order': 1423, 'expertise': 792, 'ability': 77, 'perform': 1480, 'job': 1124, 'duties': 692, 'automotive': 259, 'gaskets': 910, 'seals': 1810, 'made': 1211, 'silicone': 1867, 'rubber': 1767, 'extrusion': 803, 'lines': 1190, 'resolved': 1726, 'issues': 1112, 'parts': 1461, 'headed': 961, 'runs': 1772, 'scheduled': 1794, 'appropriate': 201, 'shifts': 1854, 'changeovers': 379, 'changes': 380, 'improvements': 1018, 'audits': 251, 'materials': 1249, 'presented': 1541, 'documents': 667, 'quotas': 1640, 'were': 2232, 'fulfilled': 894, 'monitoring': 1321, 'confirming': 496, 'stocked': 1944, 'published': 1614, 'visual': 2207, 'standards': 1927, 'vps': 2211, 'assure': 242, 'employees': 721, 'conducted': 490, 'tests': 2058, 'products': 1573, 'properties': 1594, 'validate': 2177, 'measure': 1257, 'required': 1719, 'iso': 1108, '9000': 71, 'organic': 1426, 'esters': 761, 'hydrogenated': 993, 'tallow': 2019, 'jojoba': 1128, 'oils': 1396, 'provided': 1609, 'checks': 390, 'distillation': 657, 'columns': 438, 'chillers': 394, 'reactors': 1656, 'tanks': 2021, 'boilers': 303, 'prillers': 1548, 'between10': 286, 'craft': 547, 'union': 2145, 'monitored': 1320, 'laboratory': 1144, 'experimentation': 789, 'documentation': 664, 'same': 1778, 'conductivity': 493, 'while': 2237, 'decreasing': 590, 'graphene': 934, 'loading': 1194, '85': 67, 'increased': 1028, 'epoxy': 752, 'mechanical': 1260, 'strength': 1957, 'introducing': 1088, 'processed': 1560, 'taking': 2018, 'raman': 1644, 'spectrum': 1911, 'sem': 1822, 'tem': 2046, 'analyzed': 178, 'data': 576, 'recommendations': 1664, 'resulted': 1736, 'producing': 1569, 'better': 284, 'value': 2181, 'lead': 1160, 'developing': 628, 'technology': 2041, 'transfer': 2108, 'packages': 1452, 'manufactures': 1235, 'technical': 2034, 'expert': 791, 'specific': 1908, 'oled': 1398, 'led': 1168, 'kilo': 1137, 'scale': 1790, 'campaigns': 348, 'planning': 1507, 'qualification': 1626, 'analyses': 173, 'rapid': 1647, 'commercialization': 443, 'optimized': 1418, '12l': 9, '22l': 28, 'vacuum': 2176, 'column': 437, 'meet': 1263, 'reproduce': 1715, 'qualified': 1627, 'karl': 1132, 'fischer': 846, 'titration': 2085, 'chromatography': 400, 'synthesis': 2008, 'utilizing': 2175, 'pilot': 1500, 'reviewed': 1748, 'guidelines': 950, 'member': 1268, 'hygiene': 994, 'focus': 861, 'group': 944, 'drafted': 679, 'sops': 1900, 'psms': 1612, 'green': 940, 'belt': 282, 'optimization': 1416, 'operated': 1404, 'story': 1949, 'reactions': 1654, 'numerous': 1377, 'financial': 837, 'each': 694, 'assignment': 233, 'clerical': 412, 'responsibilities': 1731, 'writing': 2264, 'reports': 1712, 'certificates': 374, 'analysis': 174, 'encouraged': 728, 'coordinated': 531, 'transactions': 2107, 'between': 285, 'scientists': 1801, 'business': 331, 'professionals': 1575, 'created': 549, 'user': 2170, 'interface': 1077, 'think': 2073, 'do': 662, 'programming': 1585, 'software': 1888, 'my': 1344, 'skills': 1879, 'performing': 1483, 'simple': 1869, 'extensive': 798, 'repairs': 1704, 'reactor': 1655, 'glassware': 926, 'pumps': 1615, 'centrifuges': 372, 'instruments': 1064, 'analytical': 175, 'ir': 1106, 'nmr': 1364, 'gc': 916, 'hplc': 988, 'determine': 624, 'composition': 469, 'gathering': 914, 'entering': 743, 'analysed': 172, 'report': 1709, 'result': 1735, 'vendors': 2191, 'study': 1970, 'kedah': 1134, 'refinery': 1681, 'hrh': 989, 'residue': 1723, 'upgrading': 2157, 'gasoline': 911, 'capacity': 354, 'tehran': 2042, 'adding': 112, 'condensate': 486, 'feed': 827, 'root': 1763, 'cause': 365, 'fouling': 883, 'heat': 966, 'exchanger': 774, 'desalter': 611, 'atmospheric': 244, 'unit': 2147, 'cooperated': 528, 'extraction': 800, 'system': 2009, 'bench': 283, 'separate': 1831, 'asphaltene': 221, 'bottom': 311, 'screen': 1805, 'companies': 452, 'facilitated': 807, 'learning': 1165, 'students': 1967, 'academic': 82, 'highest': 972, 'attendance': 245, 'spring': 1917, 'semester': 1823, 'course': 544, 'tutees': 2128, 'note': 1372, 'management': 1227, 'tutoring': 2130, 'session': 1842, 'structure': 1963, 'student': 1966, 'used': 2169, 'logic': 1199, 'reasoning': 1660, 'identify': 999, 'strengths': 1958, 'weaknesses': 2220, 'alternative': 164, 'solutions': 1895, 'approaches': 200, '95': 73, 'positive': 1524, 'surveys': 2000, 'outcome': 1436, 'fall': 813, '14': 10, 'semesters': 1824, 'daily': 573, 'sessions': 1843, 'darpa': 574, 'responsible': 1733, 'formulations': 879, 'method': 1279, 'sample': 1779, 'sterilization': 1942, 'clotting': 418, 'internal': 1081, 'injuries': 1046, 'battle': 274, 'tested': 2056, 'optimize': 1417, 'component': 465, 'choices': 396, 'catalysts': 364, 'surfactant': 1997, 'methods': 1282, 'including': 1024, 'expansion': 782, 'laser': 1149, 'scanner': 1791, 'instron': 1058, 'compression': 471, 'force': 865, 'displacement': 654, 'uptake': 2161, 'became': 277, 'key': 1136, 'operator': 1409, 'delivery': 598, 'systems': 2010, 'included': 1023, 'running': 1771, 'gage': 906, 'porcine': 1521, 'animal': 183, 'studies': 1969, 'boston': 309, 'hospital': 983, 'supply': 1992, 'authored': 254, 'instruction': 1060, '10993': 4, 'cytotoxicity': 572, 'acquisition': 100, 'nos': 1370, 'assembled': 222, 'semi': 1825, 'annual': 184, 'prepared': 1534, 'charts': 389, 'trend': 2116, 'graphs': 938, 'action': 103, 'installed': 1057, 'zebra': 2278, 'mussel': 1341, 'abatement': 76, 'started': 1929, 'conners': 501, 'creek': 553, 'after': 134, 'adhered': 115, 'policies': 1518, 'no': 1365, 'derates': 610, 'chemistry': 393, 'approximately': 203, 'ten': 2050, 'ups': 2160, 'capital': 355, 'modern': 1311, 'applications': 196, 'java': 1121, 'boot': 308, 'sql': 1918, 'server': 1837, 'microservices': 1288, 'web': 2223, 'services': 1840, 'incl': 1021, 'rest': 1734, 'soap': 1886, 'wsdl': 2267, 'xml': 2269, 'soa': 1885, 'pivotal': 1502, 'cloud': 419, 'foundry': 885, 'platform': 1511, 'gradle': 932, 'github': 925, 'continuously': 513, 'integrated': 1068, 'deployed': 606, 'updated': 2154, 'integration': 1070, 'deployment': 607, 'scripts': 1806, 'necessary': 1352, 'practices': 1529, 'consulted': 508, 'manager': 1228, 'minimal': 1297, 'viable': 2199, 'decomposed': 587, 'feature': 823, 'small': 1881, 'scoped': 1803, 'stories': 1948, 'supported': 1994, 'codex': 428, 'testing': 2057, 'processes': 1561, 'verified': 2195, 'met': 1276, 'existing': 780, 'collaborated': 430, 'innovations': 1049, 'identified': 998, 'measured': 1258, 'heavy': 967, 'concentration': 479, 'structures': 1965, 'university': 2150, 'hackathon': 951, 'two': 2131, 'consecutive': 502, 'years': 2272, 'mock': 1305, 'service': 1839, 'app': 194, 'senior': 1827, 'scholar': 1798, 'text': 2060, 'adventure': 123, 'game': 907, 'graphical': 936, 'python': 1623, 'intern': 1080, 'dr': 678, 'richard': 1756, 'males': 1221, 'cincinnati': 401, 'oh': 1394, 'november': 1373, '2013': 25, 'january': 1119, 'reformatting': 1682, 'excel': 771, 'files': 833, 'flood': 856, 'rates': 1649, 'how': 987, 'they': 2072, 'building': 327, 'tutor': 2129, 'middle': 1289, 'school': 1799, 'east': 698, 'end': 730, 'youth': 2277, 'proficient': 1578, 'ii': 1004, 'introduction': 1089, 'concepts': 482, 'mathematics': 1250, 'principles': 1550, 'imperative': 1011, 'great': 939, 'theoretical': 2068, 'ideas': 996, 'computer': 475, 'science': 1800, 'make': 1219, 'android': 181, 'apps': 204, 'navcog': 1349, 'toolthat': 2089, 'uses': 2172, 'sensors': 1830, 'vision': 2205, 'crowdsourcing': 556, 'help': 968, 'blind': 295, 'people': 1477, 'move': 1333, 'spaces': 1905, 'target': 2023, 'effort': 709, 'create': 548, 'modelsof': 1309, 'buildings': 328, 'maintain': 1214, 'person': 1487, 'teamdeveloping': 2032, 'mobile': 1303, 'andwear': 182, 'forchorus': 867, 'webbased': 2224, 'conversational': 525, 'assistant': 236, 'has': 955, 'texttospeechand': 2061, 'speechtotext': 1912, 'capabilities': 352, 'yelp': 2273, 'search': 1811, 'yahoo': 2270, 'apis': 193, 'natural': 1348, 'language': 1146, 'processor': 1563, 'tool': 2088, 'be': 276, 'added': 111, 'chorus': 398, 'fight': 832, 'gender': 920, 'violence': 2204, 'bystander': 334, 'effect': 703, 'bluetooth': 299, 'messaging': 1275, 'users': 2171, 'anonymously': 187, 'post': 1525, 'situation': 1875, 'functionality': 899, 'state': 1932, 'level': 1173, 'prescription': 1538, 'drug': 686, 'needs': 1355, 'custom': 567, 'migrated': 1290, 'website': 2225, 'membership': 1270, 'asp': 218, 'net': 1357, 'regarding': 1683, 'networking': 1359, 'wired': 2245, 'wireless': 2246, 'dialup': 640, 'email': 716, 'carnegie': 361, 'mellon': 1267, 'answered': 189, 'questions': 1636, 'about': 79, 'ms': 1334, 'office': 1391, 'communicated': 448, 'customers': 569, 'telephone': 2044, 'face': 805, 'old': 1397, 'code': 425, 'delivering': 597, 'tailored': 2015, 'news': 1362, 'coded': 426, 'model': 1306, 'controller': 521, 'architecture': 206, 'adjusted': 117, 'calibrated': 342, 'aligned': 154, 'modified': 1313, 'records': 1667, 'cabinet': 335, 'closely': 416, 'ensure': 740, 'all': 156, 'are': 207, 'troubleshooting': 2121, 'solving': 1899, 'hardware': 953, 'linux': 1191, 'os': 1432, 'centos': 371, 'suse': 2002, 'red': 1669, 'hat': 956, 'windows': 2243, 'w2k3': 2212, 'w2k8': 2213, 'log': 1198, 'failures': 812, 'supporting': 1995, 'failure': 811, 'rack': 1641, 'mount': 1331, 'x86_64': 2268, 'brick': 317, 'servers': 1838, 'established': 759, 'redesigning': 1671, '286': 32, 'computers': 477, '486': 49, 'market': 1242, 'determined': 625, '1500': 14, 'opposed': 1412, 'purchasing': 1617, 'prioritizing': 1553, 'priority': 1554, 'requests': 1718, 'would': 2262, 'impacted': 1009, 'if': 1003, 'another': 188, 'request': 1716, 'period': 1484, 'maintenance': 1217, 'network': 1358, 'database': 577, 'researched': 1722, 'preparation': 1533, 'joint': 1126, 'tactical': 2014, 'common': 446, 'operational': 1407, 'picture': 1499, 'cop': 534, 'workstation': 2256, 'jtcw': 1130, 'evaluation': 764, 'professional': 1574, 'coordinator': 533, 'program': 1583, 'hires': 975, 'division': 660, 'policy': 1519, 'cmmi': 420, 'improvement': 1017, 'research': 1721, 'alternatives': 165, 'procurement': 1566, 'dod': 668, 'modeling': 1307, 'simulation': 1870, 'ssca': 1919, 'lean': 1163, 'six': 1876, 'sigma': 1863, 'repository': 1713, 'sharepoint': 1849, 'event': 766, 'officers': 1392, 'main': 1212, 'frame': 888, 'its': 1116, 'connected': 498, 'peripherals': 1485, 'junior': 1131, 'maintaining': 1216, 'agenda': 137, 'highlighted': 973, 'topics': 2091, 'discussions': 653, 'seminars': 1826, 'related': 1690, 'transport': 2113, 'fully': 896, 'functional': 898, 'repaired': 1702, 'errors': 758, 'desk': 618, '2003': 21, 'mainframe': 1213, 'technician': 2035, 'unix': 2151, 'infrastructure': 1040, 'routers': 1764, 'access': 84, 'points': 1516, 'cabling': 338, 'administrating': 119, 'updating': 2156, 'labs': 1145, 'factory': 810, 'fixtures': 851, 'both': 310, 'acceptance': 83, 'unique': 2146, 'satellite': 1782, 'industry': 1036, 'marine': 1240, 'antenna': 190, 'protection': 1604, 'switch': 2006, 'tcp': 2029, 'ip': 1103, 'remote': 1697, 'millennium': 1294, 'macs': 1210, 'monitor': 1319, 'venture': 2192, 'embedded': 718, 'consultants': 507, 'datapath': 578, 'it': 1113, 'now': 1374, 'been': 279, 'forty': 882, 'military': 1292, 'sites': 1873, 'germany': 924, 'bahrain': 267, 'kuwait': 1140, 'qatar': 1625, 'uae': 2133, 'multiple': 1338, 'subcontractor': 1972, 'personnel': 1490, 'domestic': 670, 'foreign': 871, 'installations': 1056, 'integrating': 1069, 'include': 1022, 'smiths': 1883, 'stratos': 1953, 'global': 927, 'dts': 689, 'comsat': 478, 'rsi': 1766, 'ilx': 1005, 'lightwave': 1186, 'cca': 366, 'black': 293, 'river': 1759, 'smd': 1882, 'jan': 1118, 'aug': 252, 'masters': 1246, 'nasa': 1347, 'space': 1904, 'station': 1935, 'rfid': 1753, 'tracking': 2100, 'dec': 585, 'aided': 145, 'professors': 1576, '41': 45, 'firstyear': 845, 'basics': 272, 'guided': 949, 'class': 406, 'document': 663, 'usable': 2166, 'interactions': 1075, 'flows': 860, 'features': 824, 'itunes': 1117, 'ideated': 997, 'interfaces': 1078, 'major': 1218, 'commerce': 442, 'brands': 314, 'devised': 633, 'results': 1738, 'conception': 481, 'launch': 1154, 'wikis': 2241, 'blogs': 297, 'social': 1887, 'networks': 1360, 'contributed': 519, 'groundbreaking': 943, 'showcased': 1858, 'forthcoming': 880, 'publication': 1613, 'develop': 626, 'individualized': 1032, 'websites': 2226, 'range': 1645, 'divisions': 661, 'across': 101, 'assist': 235, 'administration': 120, 'campus': 349, 'intranet': 1086, 'calendar': 341, 'gave': 915, 'weekly': 2229, 'lectures': 1167, 'enrolled': 739, 'advanced': 121, 'introductory': 1090, 'physics': 1498, 'explained': 794, 'complex': 462, 'setting': 1846, 'grade': 931, 'examinationsheld': 768, 'hours': 985, 'individual': 1031, 'discussion': 652, 'air': 148, 'standard': 1925, 'evdo': 765, 'super': 1982, 'cell': 368, 'without': 2250, 'impacting': 1010, 'integrity': 1071, 'mobility': 1304, 'recognized': 1662, 'verizon': 2196, 'usa': 2165, 'alcatel': 150, 'kddi': 1133, 'japan': 1120, 'lab': 1142, 'members': 1269, 'providing': 1611, 'quick': 1637, 'reported': 1710, 'object': 1378, 'framework': 889, 'resource': 1727, 'vast': 2186, 'distributed': 658, 'real': 1658, 'fault': 819, 'tolerance': 2087, 'redundancy': 1677, 'resources': 1728, 'significantly': 1866, 'security': 1817, 'transmission': 2112, 'call': 345, 'setup': 1847, 'selection': 1820, 'distribution': 659, 'sdu': 1808, 'channel': 382, 'cdma': 367, 'card': 358, 'higher': 971, 'rate': 1648, 'element': 715, 'availability': 261, 'relational': 1691, 'oracle': 1422, 'billing': 291, 'computation': 473, 'subscriber': 1974, '100': 2, '000': 0, 'implementation': 1012, 'is': 1107, 'employed': 720, 'date': 579, 'allows': 161, 'faster': 818, 'conducting': 491, 'large': 1148, 'hiv': 978, 'patients': 1465, 'finding': 840, 'temporal': 2049, 'patterns': 1467, 'among': 167, 'gene': 921, 'mutations': 1342, 'drugs': 687, 'clinical': 415, 'outcomes': 1437, 'implementing': 1014, 'mining': 1298, 'algorithm': 152, 'pattern': 1466, 'discovery': 650, 'will': 2242, 'also': 163, 'querying': 1634, 'statistical': 1936, 'aggregation': 140, 'visualization': 2208, 'algorithms': 153, 'combinatorial': 439, 'biological': 292, 'arising': 210, 'string': 1960, 'matching': 1247, 'sequence': 1833, 'alignment': 155, 'fingerprint': 842, 'methodologies': 1280, 'analyzing': 179, 'correlated': 540, 'discrete': 651, 'or': 1421, 'have': 957, 'bayes': 275, 'rule': 1768, 'classify': 408, 'microarray': 1286, 'several': 1848, 'processing': 1562, 'hybridization': 992, 'construct': 504, 'mysql': 1345, 'experimental': 788, 'http': 990, 'alglab1': 151, 'cs': 561, 'ucr': 2135, 'edu': 702, 'ofrg': 1393, 'train': 2104, 'organize': 1429, 'regular': 1686, 'meetings': 1265, 'present': 1539, 'lectured': 1166, 'upper': 2159, 'undergraduate': 2138, 'composing': 468, 'syllabus': 2007, 'assigning': 232, 'homework': 982, 'preparing': 1535, 'quizzes': 1639, 'final': 835, 'exams': 769, 'supervise': 1983, 'studied': 1968, 'functions': 902, 'situ': 1874, 'images': 1007, 'mouse': 1332, 'brain': 313, 'computational': 474, 'expression': 797, 'image': 1006, 'estimating': 762, 'metastatic': 1278, 'tumor': 2124, 'cells': 369, 'pharmaceutical': 1492, 'csc': 562, '111': 5, 'question': 1635, 'may': 1255, 'timesheet': 2084, 'run': 1770, 'spent': 1914, 'quickbooks': 1638, 'exporting': 796, 'fixing': 850, 'bugs': 325, 'gui': 946, 'php': 1496, 'jmol': 1123, 'molecular': 1317, 'visualizer': 2209, 'integrate': 1067, 'kinari': 1138, 'predict': 1531, 'observed': 1381, 'crystalline': 560, 'exhibit': 779, 'auxetic': 260, 'behavior': 280, 'vax': 2187, 'vms': 2210, 'machine': 1208, 'understanding': 2141, 'ingres': 1042, 'equal': 753, 'preprocessor': 1536, 'flight': 854, 'schedules': 1795, 'find': 839, 'peak': 1473, 'frequency': 890, 'input': 1051, 'marinco': 1239, 'array': 212, 'board': 300, 'vectrix': 2189, 'graphics': 937, 'automata': 256, 'theory': 2069, 'formal': 874, 'languages': 1147, 'artificial': 215, 'intelligence': 1073, 'terminal': 2053, 'proffering': 1577, 'solution': 1894, 'militates': 1293, 'against': 135, 'optimal': 1415, 'managing': 1229, 'multidisciplinary': 1337, 'involves': 1102, 'provides': 1610, 'supervises': 1985, '40': 42, 'computerized': 476, 'cmms': 421, 'preventive': 1544, 'predictive': 1532, 'achieved': 96, '50': 50, 'reduction': 1676, 'routine': 1765, 'timely': 2082, 'lasting': 1150, 'breakdown': 316, 'well': 2231, 'unexpected': 2143, 'downtime': 674, '60': 53, 'inspections': 1054, 'respond': 1730, 'manner': 1230, 'turnover': 2127, 'closeout': 417, 'installation': 1055, 'compressors': 472, 'modification': 1312, 'pressure': 1542, 'vessel': 2198, 'patent': 1464, 'pending': 1476, 'takeoff': 2017, 'bring': 318, 'store': 1947, 'shelves': 1853, 'displays': 655, 'shelf': 1852, 'edge': 701, 'sight': 1862, 'interactive': 1076, 'concept': 480, 'manufacturing': 1236, 'months': 1326, 'leveraged': 1175, 'prototyping': 1607, 'turn': 2125, 'retail': 1739, 'producer': 1568, 'cable': 336, 'department': 603, 'flow': 859, 'workstations': 2257, 'non': 1367, 'conductive': 492, 'entertainment': 744, 'panels': 1456, 'drafting': 680, '3000': 37, 'amp': 168, 'welding': 2230, 'operations': 1408, 'need': 1353, 'purchased': 1616, 'fasteners': 817, 'sheet': 1851, 'metal': 1277, 'designing': 615, 'enclosures': 726, 'fit': 847, 'form': 872, 'function': 897, 'outgoing': 1438, 'meeting': 1264, 'short': 1857, 'turnaround': 2126, 'times': 2083, 'erp': 757, 'epicor': 751, 'assign': 230, 'indicate': 1030, 'presentations': 1540, 'units': 2149, 'surge': 1998, 'pdu': 1472, 'modular': 1314, 'vertical': 2197, 'allowed': 159, 'day': 580, 'placed': 1504, 'housing': 986, 'generated': 923, '3d': 41, 'models': 1308, 'drawings': 683, 'artwork': 216, 'associated': 239, 'uninterruptable': 2144, 'provide': 1608, 'suppliers': 1990, 'gangway': 908, 'riyadh': 1760, 'saudi': 1785, 'arabia': 205, 'metro': 1285, 'choose': 397, 'supplier': 1989, 'assessments': 227, 'bogie': 302, 'sao': 1780, 'paulo': 1468, 'brazil': 315, 'monorail': 1322, 'designs': 616, 'being': 281, 'queries': 1633, 'accordingly': 88, 'electromechanical': 713, 'leadership': 1161, 'proofreading': 1592, 'intellectual': 1072, 'property': 1595, 'assessment': 226, 'documented': 665, 'applied': 197, 'solid': 1892, 'works': 2255, 'cad': 339, 'accomplishing': 86, 'robotic': 1761, 'mechanisms': 1261, 'automated': 257, 'tape': 2022, 'library': 1178, 'supplies': 1991, 'assessed': 225, 'manufacture': 1232, 'musical': 1340, 'instrument': 1063, 'device': 631, 'aspects': 219, 'developments': 630, 'modems': 1310, 'gateway': 912, 'top': 2090, 'box': 312, 'drove': 685, 'save': 1786, 'current': 564, 'dfm': 635, 'dfa': 634, 'oem': 1387, 'odm': 1384, 'manufacturers': 1234, 'negotiated': 1356, 'flotherm': 858, 'pcb': 1470, 'levels': 1174, 'thermal': 2070, 'electronic': 714, 'cooling': 527, 'forced': 866, 'convection': 524, 'mentored': 1271, 'life': 1184, 'outsourcing': 1441, 'pro': 1555, 'mcad': 1256, 'drawing': 682, 'gd': 917, 'packaging': 1453, 'characterizes': 386, 'structural': 1962, 'ultra': 2136, 'survive': 2001, 'worse': 2260, 'case': 362, 'sds': 1807, 'seismic': 1818, 'effectively': 705, 'name': 1346, 'italy': 1114, 'facilitate': 806, 'transition': 2110, 'flagship': 852, '750': 61, 'kw': 1141, 'mw': 1343, 'inverter': 1092, 'characterized': 385, 'airflow': 149, 'defined': 594, 'filter': 834, 'criteria': 554, 'qualify': 1628, 'vendor': 2190, 'supplied': 1988, 'solved': 1896, 'sustaining': 2005, 'engineer': 732, 'challenges': 376, 'builds': 329, 'excellence': 772, 'full': 895, 'complement': 456, 'aesthetic': 131, 'pellvve': 1475, 'rf': 1752, 'wrinkle': 2263, 'details': 620, 'bom': 304, 'stack': 1920, 'supports': 1996, 'terms': 2054, 'continuity': 511, 'designers': 614, 'define': 593, '2d': 33, 'solidworks': 1893, 'autocad': 255, 'incorporated': 1026, 'latest': 1152, 'technologies': 2040, 'successful': 1977, 'preproduction': 1537, 'prototypes': 1606, 'ranging': 1646, 'healthcare': 964, 'cords': 535, 'cellular': 370, 'tower': 2095, 'radio': 1643, 'speed': 1913, 'assemblies': 223, 'detailed': 619, 'instructions': 1061, 'represented': 1714, 'liaison': 1177, 'article': 214, 'blueprints': 298, 'programmed': 1584, 'codes': 427, 'verification': 2194, 'signal': 1864, 'inspection': 1053, 'accountability': 89, 'bill': 289, 'specializes': 1906, 'wide': 2240, 'scope': 1802, 'loudspeaker': 1203, 'changing': 381, 'sound': 1901, 'adaptation': 109, 'floor': 857, 'lay': 1156, 'out': 1435, 'balancing': 269, 'machines': 1209, '12': 7, 'workers': 2253, 'calculations': 340, 'sketches': 1878, 'comparisons': 454, 'similar': 1868, 'mark': 1241, 'measurements': 1259, 'options': 1420, 'found': 884, 'assigned': 231, 'proper': 1593, 'ground': 942, 'telephony': 2045, 'devices': 632, 'digital': 643, 'analog': 171, '98': 74, 'ac': 81, 'dc': 582, 'repairing': 1703, 'circuits': 404, 'down': 673, 'schematics': 1797, 'approved': 202, 'but': 332, 'not': 1371, 'limited': 1187, 'suite': 1981, 'communications': 450, 'concerning': 483, 'interpreted': 1083, 'supervisors': 1986, 'encryption': 729, 'repair': 1701, 'selected': 1819, 'pool': 1520, 'competing': 455, 'serve': 1835, 'outside': 1440, 'agencies': 136, 'organizations': 1428, 'exceeded': 770, '90': 70, 'readiness': 1657, 'rating': 1650, 'sensitive': 1829, 'communication': 449, 'entire': 745, 'length': 1170, 'employment': 722, 'fiber': 830, 'optic': 1413, 'audio': 249, 'aids': 146, 'soldered': 1890, 'connections': 499, 'spliced': 1915, 'wiring': 2247, 'assets': 229, 'back': 266, 'owning': 1449, 'sections': 1813, '99': 75, 'uptime': 2162, 'secret': 1812, 'clearance': 411, 'sustained': 2004, 'entirety': 746, 'enlistment': 738, 'trn': 2119, '47': 48, 'tacan': 2013, 'oef122': 1385, 'oef133': 1386, 'afghanistan': 132, 'tpq': 2096, '44': 46, 'metmfr': 1283, 'doppler': 671, 'radar': 1642, 'weather': 2222, 'troubleshoot': 2120, 'prc': 1530, '117': 6, 'sets': 1845, 'manuals': 1231, 'correct': 538, 'utilized': 2174, 'supervisory': 1987, 'completely': 459, 'resigned': 1724, 'temperature': 2047, 'controllers': 522, 'much': 1335, 'iec': 1002, '61010': 55, 'ipc': 1104, '600': 54, 'ipc2221': 1105, 'redesign': 1670, 'circuitry': 403, 'travelers': 2114, 'our': 1434, 'warranty': 2215, 'returns': 1743, 'zero': 2279, 'advertising': 124, 'attending': 247, 'trade': 2101, 'shows': 1859, 'quarterly': 1632, '2000': 20, 'overhead': 1445, 'entry': 747, 'experimented': 790, 'chose': 399, 'gel': 919, '80': 62, 'percent': 1479, 'still': 1943, 'kept': 1135, 'bonding': 305, 'lowest': 1204, 'lcd': 1158, 'touch': 2093, 'panel': 1455, 'ad': 108, 'firmware': 843, 'prototype': 1605, 'validation': 2179, 'fabricating': 804, 'pcbs': 1471, 'connectors': 500, 'cables': 337, 'layouts': 1157, 'eagle': 695, 'manufactured': 1233, 'them': 2066, 'lpkf': 1205, 'milling': 1295, 'noise': 1366, 'humidity': 991, 'sensing': 1828, 'guide': 948, 'debugging': 584, 'matlab': 1251, 'makerbot': 1220, 'replicator': 1708, '2x': 34, 'printer': 1551, '38m': 40, 'army': 211, 'corps': 537, 'contractor': 515, 'diagrams': 638, 'load': 1193, 'phases': 1494, 'rfis': 1754, 'revise': 1750, 'redlines': 1672, 'recommendation': 1663, 'government': 930, 'wallops': 2214, 'harness': 954, 'nonconformance': 1368, 'dispositions': 656, 'evaluate': 763, 'streamline': 1954, 'most': 1328, 'wire': 2244, 'assurance': 241, 'qa': 1624, 'pointscompliant': 1517, 'external': 799, 'specification': 1909, 'std': 1938, '8739': 68, 'jpl': 1129, '8208': 64, 'mil': 1291, 'hdbk': 960, '83575': 66, 'whma': 2238, '620': 56, 'instructed': 1059, 'colleague': 434, 'infusion': 1041, 'siebel': 1861, 'conformed': 497, 'fda': 821, 'flogard': 855, 'commanding': 441, 'deliver': 595, 'status': 1937, 'mission': 1300, 'convey': 526, 'understandable': 2140, 'condition': 487, 'long': 1200, 'able': 78, 'communicate': 447, 'malfunction': 1222, 'feedback': 828, 'said': 1775, 'verbal': 2193, 'coordinate': 530, 'updates': 2155, 'procomm': 1564, 'purpose': 1619, 'defective': 592, 'familiarity': 814, 'environment': 748, 'individuals': 1033, 'toward': 2094, 'aimed': 147, 'earned': 697, 'desirable': 617, 'whereby': 2235, 'demonstrating': 602, 'pass': 1462, 'analyze': 177, 'worldwide': 2259, 'corrective': 539, 'preventative': 1543, 'avionics': 263, 'equaling': 754, 'man': 1224, 'sea': 1809, 'hawk': 958, 'inter': 1074, 'locations': 1197, 'navigation': 1350, 'subsystems': 1975, 'stood': 1945, 'hour': 984, 'watches': 2218, 'safe': 1773, 'transit': 2109, 'countless': 543, 'subordinates': 1973, 'cleaned': 409, 'place': 1503, 'areas': 209, 'shop': 1856, 'lavatories': 1155, 'stairwells': 1923, 'strategically': 1951, 'steered': 1940, 'maximize': 1252, 'fertilizer': 829, 'strict': 1959, 'rules': 1769, 'types': 2132, 'lights': 1185, 'plugs': 1513, 'smoke': 1884, 'detectors': 623, 'five': 848, 'accurately': 94, 'steel': 1939, 'pvc': 1621, 'conduit': 494, 'motors': 1330, 'brought': 322, 'collaboration': 432, 'canadian': 350, 'vilholth': 2203, 'jensen': 1122, 'associates': 240, 'ltd': 1206, 'sub': 1971, 'contractors': 516, 'signals': 1865, 'microcontrollers': 1287, 'graphic': 935, 'lcds': 1159, 'diagnosis': 636, 'isolation': 1110, 'adjustments': 118, 'removal': 1698, 'variety': 2184, 'troubleshot': 2122, 'onsite': 1401, 'calibration': 343, 'environments': 750, 'unscheduled': 2152, 'effective': 704, 'enhance': 736, 'physical': 1497, 'demanding': 600, 'programs': 1586, 'ami': 166, 'aviation': 262, 'block': 296, 'automatic': 258, 'optimum': 1419, 'success': 1976, 'secure': 1815, 'video': 2200, 'teleconference': 2043, 'embarked': 717, 'world': 2258, 'tracing': 2097, 'isolate': 1109, 'faulty': 820, 'cryptographic': 559, 'additional': 114, 'modules': 1315, 'amplifiers': 169, 'single': 1871, 'ship': 1855, 'replacements': 1706, 'efficient': 708, 'nuclear': 1375, 'scheduling': 1796, 'encourage': 727, '150': 13, 'coordinating': 532, 'open': 1402, 'departments': 604, 'conserve': 503, 'labor': 1143, 'documenting': 666, 'startup': 1931, 'shutdown': 1860, 'streamlined': 1955, 'replacing': 1707, 'expectations': 783, 'completing': 460, 'dozens': 677, 'ahead': 144, 'early': 696, 'reporting': 1711, 'forms': 875, 'adapted': 110, 'diagnostic': 637, 'cervical': 375, 'cancer': 351, 'detection': 622, 'detecting': 621, 'composed': 467, 'co': 422, 'primary': 1549, 'accordance': 87, 'trials': 2117, 'advisor': 128, 'retirement': 1740, 'investment': 1096, 'advice': 125, 'estate': 760, 'tax': 2027, 'strategies': 1952, 'highly': 974, 'practice': 1528, 'trades': 2102, 'serving': 1841, 'aum': 253, 'satisfaction': 1783, '88': 69, 'fantastic': 815, 'personalized': 1489, 'every': 767, '91': 72, 'partnered': 1459, 'parent': 1457, 'goals': 929, 'objectives': 1379, 'portfolios': 1523, '400': 43, '17': 15, 'care': 359, 'equity': 756, 'discover': 649, 'undervalued': 2142, 'investments': 1097, 'reasonable': 1659, 'prospects': 1603, 'term': 2052, 'sustainable': 2003, 'growth': 945, 'portfolio': 1522, 'regularly': 1687, 'prospective': 1602, 'personal': 1488, 'approach': 199, 'trust': 2123, 'emphasized': 719, 'investor': 1098, 'recommended': 1665, 'collaborating': 431, 'functioning': 901, 'forecast': 868, 'scenarios': 1792, 'drivers': 684, 'risks': 1758, 'cross': 555, 'functionally': 900, 'complete': 457, 'sap': 1781, 'bi': 288, 'cooperation': 529, 'bex': 287, 'templates': 2048, 'dashboards': 575, 'these': 2071, 'revenues': 1746, 'direct': 646, 'coming': 440, 'normalized': 1369, 'structured': 1964, 'further': 904, 'dependent': 605, 'afo': 133, 'enabled': 725, 'hoc': 981, 'analytics': 176, 'pivot': 1501, 'table': 2011, 'front': 892, 'coach': 423, 'extracts': 801, 'tables': 2012, 'obtained': 1382, 'series': 1834, '63': 57, 'minnesota': 1299, 'accident': 85, 'licensures': 1183, 'relationships': 1694, 'nearly': 1351, '300': 36, 'advising': 127, 'total': 2092, 'gross': 941, 'dealer': 583, 'concession': 485, 'gdc': 918, 'achiever': 97, 'diamond': 641, 'award': 264, 'plan': 1505, '66': 58, 'general': 922, 'hmo': 979, 'licenses': 1181, 'become': 278, 'registered': 1684, 'inputting': 1052, 'executing': 777, 'trading': 2103, 'accounts': 91, 'many': 1237, 'tasks': 2026, 'advisors': 129, 'served': 1836, 'advisory': 130, '401': 44, 'methodology': 1281, 'track': 2098, 'proprietary': 1598, 'metrics': 1284, 'number': 1376, 'art': 213, 'wealth': 2221, 'thompson': 2075, 'one': 1400, 'relationship': 1693, 'salesforce': 1777, 'invested': 1093, 'proposition': 1597, 'worth': 2261, 'hnw': 980, 'executives': 778, 'york': 2276, 'area': 208, 'fortune': 881, 'booked': 307, 'prospect': 1600, 'week': 2228, 'cold': 429, 'calling': 346, 'dials': 639, 'gathered': 913, 'comprehensive': 470, 'goal': 928, 'graduated': 933, 'ubs': 2134, 'featuring': 825, 'coursework': 545, 'capstone': 356, 'weehawken': 2227, 'nj': 1363, 'headquarters': 962, 'passed': 1463, 'regulatory': 1689, 'scores': 1804, '82': 63, '83': 65, 'respectively': 1729, 'interviewed': 1084, 'income': 1025, 'expenses': 785, 'insurance': 1065, 'coverage': 546, 'risk': 1757, 'needed': 1354, 'profiled': 1579, 'customized': 570, 'instructor': 1062, 'agents': 139, 'applying': 198, 'due': 690, 'diligence': 644, 'disability': 647, 'purposes': 1620, 'taken': 2016, 'sold': 1889, 'insurances': 1066, 'college': 436, 'funding': 903, 'pmd': 1514, 'awards': 265, 'dinner': 645, '30million': 38, 'dollars': 669, 'annuity': 186, 'book': 306, 'source': 1902, 'cultivated': 563, 'merrill': 1274, 'lynch': 1207, 'investing': 1095, 'suitable': 1980, 'banking': 270, 'lending': 1169, 'asset': 228, 'allocation': 157, 'strategic': 1950, 'corporate': 536, 'reevaluate': 1679, 'projected': 1589, 'advantage': 122, 'brokerage': 320, 'deepen': 591, 'offer': 1389, 'advised': 126, 'annually': 185, 'texas': 2059, 'renewed': 1699, 'license': 1179, 'satisfied': 1784, 'healthy': 965, 'prospected': 1601, 'contacts': 509, 'community': 451, 'phone': 1495, 'calls': 347, 'referrals': 1680, 'triple': 2118, 'crown': 557, 'surpassing': 1999, 'partnership': 1460, '140': 11, 'jointly': 1127, 'doubling': 672, 'less': 1171, 'actively': 105, 'conditions': 488, 'money': 1318, 'bringing': 319, '20mm': 27, '2012': 24, 'opening': 1403, 'quantitative': 1630, 'sharpe': 1850, 'ratio': 1651, 'alpha': 162, 'hypothetical': 995, 'monte': 1323, 'carlo': 360, 'actionable': 104, 'focusing': 863, 'sector': 1814, 'classes': 407, 'mlps': 1302, 'experienced': 787, 'investors': 1099, 'monthly': 1325, 'package': 1451, 'lauded': 1153, 'mentoring': 1272, 'whom': 2239, 'redundant': 1678, 'accurate': 93, 'initiated': 1044, 'recording': 1666, 'payor': 1469, 'claim': 405, 'allowances': 158, 'audit': 250, 'findings': 841, 'tenure': 2051, 'controls': 523, 'strong': 1961, 'relations': 1692, 'marketing': 1244, 'achieve': 95, 'revenue': 1745, 'agent': 138, 'acquiring': 99, 'jobs': 1125, 'inventory': 1091, 're': 1653, 'ordering': 1424, 'when': 2233, 'certain': 373, '2008': 22, 'history': 977, 'downturn': 675, 'aggressive': 141, 'containment': 510, 'secured': 1816, 'financing': 838, 'contracts': 517, 'focused': 862, 'received': 1661, 'repeat': 1705, 'standardized': 1926, 'budgeting': 324, 'forecasting': 870, 'accounting': 90, 'variance': 2183, 'responsibility': 1732, 'valuation': 2180, 'profitability': 1581, '70': 59, 'assisting': 238, 'merger': 1273, 'master': 1245, 'blenders': 294, '1753': 16, 'liaised': 1176, 'pwc': 1622, 'requested': 1717, 'days': 581, 'outstanding': 1442, 'initial': 1043, 'invoice': 1100, '5m': 52, 'billed': 290, 'tracked': 2099, 'orders': 1425, 'thus': 2080, 'late': 1151, 'disconnect': 648, 'credits': 552, 'contractual': 518, 'slas': 1880, 'agreements': 143, '25m': 31, 'quarter': 1631, 'adherence': 116, 'brokers': 321, 'expanding': 781, 'opportunities': 1411, 'loan': 1195, 'projections': 1590, 'credit': 551, 'loans': 1196, 'maximizing': 1253, 'relatively': 1695, 'collected': 435, 'rents': 1700, 'deposits': 608, 'owners': 1448, 'written': 2265, 'vba': 2188, 'chart': 388, 'drastically': 681, 'influenced': 1038, 'historical': 976, 'finances': 836, 'regression': 1685, 'forecasted': 869, 'profit': 1580, 'loss': 1201, 'multivariable': 1339, 'linear': 1189, 'profits': 1582, 'solver': 1898, 'forma': 873, 'statements': 1933, 'marginal': 1238, 'point': 1515, 'pricing': 1547, 'demand': 599, 'curve': 566, 'allowing': 160, 'understand': 2139, 'price': 1546, 'elasticity': 711}

def predict(doc):
    doc_array = np.zeros((1, vc.shape[1]))
    words = my_tokenizer(doc)
    for word in words:
        if word in vocab.keys():
            doc_array[0, vocab[word]] += 1
    y = model.predict(doc_array)
    return {'result': y}