# Sample Types
types = [
    "Electronics", "Cameras", "Computers", "Laptops", "Smartphones", 
    "Tablets", "Accessories", "Networking", "Printers", "Scanners",
    "Software", "Monitors", "Storage", "Memory", "Power Supply",
    "Keyboards", "Mice", "Webcams", "Headsets", "Speakers",
    "Microphones", "Drones", "Projectors", "Video Equipment", "Audio Equipment",
    "Home Appliances", "Wearable Technology", "Gaming Consoles", "VR Equipment", "Smart Home Devices",
    "3D Printers", "Graphics Cards", "Motherboards", "Processors", "Cooling Systems",
    "Cases", "Surge Protectors", "UPS", "Routers", "Modems",
    "Network Switches", "Network Adapters", "NAS", "Servers", "Server Racks",
    "Cables", "Chargers", "Docking Stations", "Mounts", "Security Systems"
]

# Sample Categories with Parent IDs
# Sample Categories with IDs and Parent IDs
categories = [
    {"id": 1, "name": "Digital Cameras", "type": "Cameras", "parent_id": None},
    {"id": 2, "name": "DSLR Cameras", "type": "Cameras", "parent_id": 1},
    {"id": 3, "name": "Mirrorless Cameras", "type": "Cameras", "parent_id": 1},
    {"id": 4, "name": "Action Cameras", "type": "Cameras", "parent_id": 2},
    {"id": 5, "name": "Camera Lenses", "type": "Cameras", "parent_id": 2},
    {"id": 6, "name": "Laptop Computers", "type": "Computers", "parent_id": None},
    {"id": 7, "name": "Desktop Computers", "type": "Computers", "parent_id": 6},
    {"id": 8, "name": "Gaming Laptops", "type": "Laptops", "parent_id": None},
    {"id": 9, "name": "Ultrabooks", "type": "Laptops", "parent_id": 8},
    {"id": 10, "name": "Chromebooks", "type": "Laptops", "parent_id": 8},
    {"id": 11, "name": "Android Phones", "type": "Smartphones", "parent_id": None},
    {"id": 12, "name": "iPhones", "type": "Smartphones", "parent_id": 11},
    {"id": 13, "name": "5G Smartphones", "type": "Smartphones", "parent_id": 11},
    {"id": 14, "name": "Smartphone Accessories", "type": "Accessories", "parent_id": None},
    {"id": 15, "name": "Tablet Computers", "type": "Tablets", "parent_id": None},
    {"id": 16, "name": "iPads", "type": "Tablets", "parent_id": 15},
    {"id": 17, "name": "Tablet Accessories", "type": "Accessories", "parent_id": 15},
    {"id": 18, "name": "WiFi Routers", "type": "Networking", "parent_id": None},
    {"id": 19, "name": "Network Switches", "type": "Networking", "parent_id": 18},
    {"id": 20, "name": "Printers", "type": "Printers", "parent_id": None},
    {"id": 21, "name": "Laser Printers", "type": "Printers", "parent_id": 20},
    {"id": 22, "name": "Inkjet Printers", "type": "Printers", "parent_id": 20},
    {"id": 23, "name": "Printer Ink", "type": "Printers", "parent_id": 21},
    {"id": 24, "name": "Scanners", "type": "Scanners", "parent_id": None},
    {"id": 25, "name": "Flatbed Scanners", "type": "Scanners", "parent_id": 24},
    {"id": 26, "name": "Sheetfed Scanners", "type": "Scanners", "parent_id": 24},
    {"id": 27, "name": "Antivirus Software", "type": "Software", "parent_id": None},
    {"id": 28, "name": "Office Software", "type": "Software", "parent_id": 27},
    {"id": 29, "name": "Graphics Software", "type": "Software", "parent_id": 27},
    {"id": 30, "name": "Photo Editing Software", "type": "Software", "parent_id": 28},
    {"id": 31, "name": "Monitors", "type": "Monitors", "parent_id": None},
    {"id": 32, "name": "4K Monitors", "type": "Monitors", "parent_id": 31},
    {"id": 33, "name": "Curved Monitors", "type": "Monitors", "parent_id": 31},
    {"id": 34, "name": "Portable Monitors", "type": "Monitors", "parent_id": 31},
    {"id": 35, "name": "External Hard Drives", "type": "Storage", "parent_id": None},
    {"id": 36, "name": "SSD Drives", "type": "Storage", "parent_id": 35},
    {"id": 37, "name": "USB Flash Drives", "type": "Storage", "parent_id": 35},
    {"id": 38, "name": "RAM Modules", "type": "Memory", "parent_id": None},
    {"id": 39, "name": "Power Supply Units", "type": "Power Supply", "parent_id": None},
    {"id": 40, "name": "Mechanical Keyboards", "type": "Keyboards", "parent_id": None},
    {"id": 41, "name": "Wireless Keyboards", "type": "Keyboards", "parent_id": 40},
    {"id": 42, "name": "Gaming Mice", "type": "Mice", "parent_id": None},
    {"id": 43, "name": "Wireless Mice", "type": "Mice", "parent_id": 42},
    {"id": 44, "name": "HD Webcams", "type": "Webcams", "parent_id": None},
    {"id": 45, "name": "4K Webcams", "type": "Webcams", "parent_id": 44},
    {"id": 46, "name": "Gaming Headsets", "type": "Headsets", "parent_id": None},
    {"id": 47, "name": "Wireless Headsets", "type": "Headsets", "parent_id": 46},
    {"id": 48, "name": "Bluetooth Speakers", "type": "Speakers", "parent_id": None},
    {"id": 49, "name": "Portable Speakers", "type": "Speakers", "parent_id": 48},
    {"id": 50, "name": "Studio Microphones", "type": "Microphones", "parent_id": None},
    {"id": 51, "name": "USB Microphones", "type": "Microphones", "parent_id": 50},
    {"id": 52, "name": "Drone Cameras", "type": "Drones", "parent_id": None},
    {"id": 53, "name": "Projectors", "type": "Projectors", "parent_id": None},
    {"id": 54, "name": "Home Theater Projectors", "type": "Projectors", "parent_id": 53},
    {"id": 55, "name": "Video Equipment", "type": "Video Equipment", "parent_id": None},
    {"id": 56, "name": "Audio Equipment", "type": "Audio Equipment", "parent_id": None},
    {"id": 57, "name": "Smart Home Hubs", "type": "Smart Home Devices", "parent_id": None},
    {"id": 58, "name": "Smart Thermostats", "type": "Smart Home Devices", "parent_id": 57},
    {"id": 59, "name": "3D Printers", "type": "3D Printers", "parent_id": None},
    {"id": 60, "name": "Graphics Cards", "type": "Graphics Cards", "parent_id": None},
    {"id": 61, "name": "Motherboards", "type": "Motherboards", "parent_id": None},
    {"id": 62, "name": "Processors", "type": "Processors", "parent_id": None},
    {"id": 63, "name": "Cooling Systems", "type": "Cooling Systems", "parent_id": None},
    {"id": 64, "name": "Computer Cases", "type": "Cases", "parent_id": None},
    {"id": 65, "name": "Surge Protectors", "type": "Surge Protectors", "parent_id": None},
    {"id": 66, "name": "Uninterruptible Power Supplies (UPS)", "type": "UPS", "parent_id": None},
    {"id": 67, "name": "Network Routers", "type": "Routers", "parent_id": None},
    {"id": 68, "name": "Network Modems", "type": "Modems", "parent_id": None},
    {"id": 69, "name": "NAS Devices", "type": "NAS", "parent_id": None},
    {"id": 70, "name": "Servers", "type": "Servers", "parent_id": None},
    {"id": 71, "name": "Server Racks", "type": "Server Racks", "parent_id": 70},
    {"id": 72, "name": "HDMI Cables", "type": "Cables", "parent_id": None},
    {"id": 73, "name": "USB Cables", "type": "Cables", "parent_id": 72},
    {"id": 74, "name": "Charging Stations", "type": "Chargers", "parent_id": None},
    {"id": 75, "name": "Docking Stations", "type": "Docking Stations", "parent_id": None},
    {"id": 76, "name": "TV Mounts", "type": "Mounts", "parent_id": None},
    {"id": 77, "name": "Security Cameras", "type": "Security Systems", "parent_id": None},
    {"id": 78, "name": "Home Security Systems", "type": "Security Systems", "parent_id": 77},
    {"id": 79, "name": "Fitness Trackers", "type": "Wearable Technology", "parent_id": None},
    {"id": 80, "name": "Smart Watches", "type": "Wearable Technology", "parent_id": 79},
    {"id": 81, "name": "Virtual Reality Headsets", "type": "VR Equipment", "parent_id": None},
    {"id": 82, "name": "VR Controllers", "type": "VR Equipment", "parent_id": 81},
    {"id": 83, "name": "Gaming Consoles", "type": "Gaming Consoles", "parent_id": None},
    {"id": 84, "name": "PlayStation Consoles", "type": "Gaming Consoles", "parent_id": 83},
    {"id": 85, "name": "Xbox Consoles", "type": "Gaming Consoles", "parent_id": 83},
    {"id": 86, "name": "Nintendo Consoles", "type": "Gaming Consoles", "parent_id": 83},
    {"id": 87, "name": "Gaming Accessories", "type": "Accessories", "parent_id": None},
    {"id": 88, "name": "Controllers", "type": "Accessories", "parent_id": 87},
    {"id": 89, "name": "Headsets", "type": "Accessories", "parent_id": 87},
    {"id": 90, "name": "External Storage", "type": "Storage", "parent_id": 35},
    {"id": 91, "name": "Solid State Drives", "type": "Storage", "parent_id": 35},
    {"id": 92, "name": "Hard Disk Drives", "type": "Storage", "parent_id": 35},
    {"id": 93, "name": "NAS Drives", "type": "Storage", "parent_id": 69},
    {"id": 94, "name": "Cloud Storage", "type": "Storage", "parent_id": 35},
    {"id": 95, "name": "Network Attached Storage", "type": "Storage", "parent_id": 69},
    {"id": 96, "name": "Backup Solutions", "type": "Storage", "parent_id": 35},
    {"id": 97, "name": "Data Recovery", "type": "Storage", "parent_id": 35},
    {"id": 98, "name": "Security Software", "type": "Software", "parent_id": 27},
    {"id": 99, "name": "Operating Systems", "type": "Software", "parent_id": 27},
    {"id": 100, "name": "Business Software", "type": "Software", "parent_id": 28},
    {"id": 101, "name": "Productivity Software", "type": "Software", "parent_id": 28},
    {"id": 102, "name": "Development Tools", "type": "Software", "parent_id": 28},
    {"id": 103, "name": "Web Browsers", "type": "Software", "parent_id": 27},
    {"id": 104, "name": "Media Players", "type": "Software", "parent_id": 28},
    {"id": 105, "name": "Audio Editing Software", "type": "Software", "parent_id": 30},
    {"id": 106, "name": "Video Editing Software", "type": "Software", "parent_id": 30},
    {"id": 107, "name": "Accounting Software", "type": "Software", "parent_id": 28},
    {"id": 108, "name": "CAD Software", "type": "Software", "parent_id": 30},
    {"id": 109, "name": "3D Modeling Software", "type": "Software", "parent_id": 30},
    {"id": 110, "name": "Digital Art Software", "type": "Software", "parent_id": 30},
    {"id": 111, "name": "Enterprise Software", "type": "Software", "parent_id": 28},
    {"id": 112, "name": "CRM Software", "type": "Software", "parent_id": 28},
    {"id": 113, "name": "ERP Software", "type": "Software", "parent_id": 28},
    {"id": 114, "name": "HR Software", "type": "Software", "parent_id": 28},
    {"id": 115, "name": "Project Management Software", "type": "Software", "parent_id": 28},
    {"id": 116, "name": "Network Management Software", "type": "Software", "parent_id": 27},
    {"id": 117, "name": "Database Software", "type": "Software", "parent_id": 27},
    {"id": 118, "name": "Email Clients", "type": "Software", "parent_id": 28},
    {"id": 119, "name": "Messaging Apps", "type": "Software", "parent_id": 28},
    {"id": 120, "name": "Communication Software", "type": "Software", "parent_id": 28},
    {"id": 121, "name": "File Sharing Software", "type": "Software", "parent_id": 27},
    {"id": 122, "name": "Desktop Publishing Software", "type": "Software", "parent_id": 30},
    {"id": 123, "name": "Presentation Software", "type": "Software", "parent_id": 28},
    {"id": 124, "name": "Remote Desktop Software", "type": "Software", "parent_id": 27},
    {"id": 125, "name": "Cloud Computing Software", "type": "Software", "parent_id": 27},
    {"id": 126, "name": "System Utilities", "type": "Software", "parent_id": 27},
    {"id": 127, "name": "Disk Management Software", "type": "Software", "parent_id": 27},
    {"id": 128, "name": "Backup Software", "type": "Software", "parent_id": 27},
    {"id": 129, "name": "Compression Software", "type": "Software", "parent_id": 27},
    {"id": 130, "name": "Virtualization Software", "type": "Software", "parent_id": 27},
    {"id": 131, "name": "Simulation Software", "type": "Software", "parent_id": 30},
    {"id": 132, "name": "Video Conferencing Software", "type": "Software", "parent_id": 28},
    {"id": 133, "name": "Voice Over IP Software", "type": "Software", "parent_id": 28},
    {"id": 134, "name": "Audio Conferencing Software", "type": "Software", "parent_id": 28},
    {"id": 135, "name": "Codecs", "type": "Software", "parent_id": 27},
    {"id": 136, "name": "Firmware", "type": "Software", "parent_id": 27},
    {"id": 137, "name": "BIOS", "type": "Software", "parent_id": 27},
    {"id": 138, "name": "Drivers", "type": "Software", "parent_id": 27},
    {"id": 139, "name": "Embedded Software", "type": "Software", "parent_id": 27},
    {"id": 140, "name": "Software Development Kits", "type": "Software", "parent_id": 27},
    {"id": 141, "name": "Libraries", "type": "Software", "parent_id": 27},
    {"id": 142, "name": "Frameworks", "type": "Software", "parent_id": 27},
    {"id": 143, "name": "APIs", "type": "Software", "parent_id": 27},
    {"id": 144, "name": "Integrated Development Environments", "type": "Software", "parent_id": 27},
    {"id": 145, "name": "Compilers", "type": "Software", "parent_id": 27},
    {"id": 146, "name": "Assemblers", "type": "Software", "parent_id": 27},
    {"id": 147, "name": "Debuggers", "type": "Software", "parent_id": 27},
    {"id": 148, "name": "Profilers", "type": "Software", "parent_id": 27},
    {"id": 149, "name": "Code Editors", "type": "Software", "parent_id": 27},
    {"id": 150, "name": "Revision Control Systems", "type": "Software", "parent_id": 27},
    {"id": 151, "name": "Build Automation Tools", "type": "Software", "parent_id": 27},
    {"id": 152, "name": "Continuous Integration Tools", "type": "Software", "parent_id": 27},
    {"id": 153, "name": "Continuous Deployment Tools", "type": "Software", "parent_id": 27},
    {"id": 154, "name": "Static Analysis Tools", "type": "Software", "parent_id": 27},
    {"id": 155, "name": "Dynamic Analysis Tools", "type": "Software", "parent_id": 27},
    {"id": 156, "name": "Code Review Tools", "type": "Software", "parent_id": 27},
    {"id": 157, "name": "Testing Frameworks", "type": "Software", "parent_id": 27},
    {"id": 158, "name": "Unit Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 159, "name": "Integration Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 160, "name": "Functional Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 161, "name": "Acceptance Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 162, "name": "Performance Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 163, "name": "Load Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 164, "name": "Stress Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 165, "name": "Usability Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 166, "name": "Compatibility Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 167, "name": "Security Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 168, "name": "Configuration Management Tools", "type": "Software", "parent_id": 27},
    {"id": 169, "name": "Provisioning Tools", "type": "Software", "parent_id": 27},
    {"id": 170, "name": "Orchestration Tools", "type": "Software", "parent_id": 27},
    {"id": 171, "name": "Monitoring Tools", "type": "Software", "parent_id": 27},
    {"id": 172, "name": "Logging Tools", "type": "Software", "parent_id": 27},
    {"id": 173, "name": "Alerting Tools", "type": "Software", "parent_id": 27},
    {"id": 174, "name": "Analytics Tools", "type": "Software", "parent_id": 27},
    {"id": 175, "name": "Business Intelligence Tools", "type": "Software", "parent_id": 27},
    {"id": 176, "name": "Data Visualization Tools", "type": "Software", "parent_id": 27},
    {"id": 177, "name": "Big Data Tools", "type": "Software", "parent_id": 27},
    {"id": 178, "name": "Machine Learning Tools", "type": "Software", "parent_id": 27},
    {"id": 179, "name": "Deep Learning Tools", "type": "Software", "parent_id": 27},
    {"id": 180, "name": "Artificial Intelligence Tools", "type": "Software", "parent_id": 27},
    {"id": 181, "name": "Robotic Process Automation Tools", "type": "Software", "parent_id": 27},
    {"id": 182, "name": "Blockchain Tools", "type": "Software", "parent_id": 27},
    {"id": 183, "name": "Cryptography Tools", "type": "Software", "parent_id": 27},
    {"id": 184, "name": "Cybersecurity Tools", "type": "Software", "parent_id": 27},
    {"id": 185, "name": "Endpoint Security Tools", "type": "Software", "parent_id": 27},
    {"id": 186, "name": "Network Security Tools", "type": "Software", "parent_id": 27},
    {"id": 187, "name": "Cloud Security Tools", "type": "Software", "parent_id": 27},
    {"id": 188, "name": "Mobile Security Tools", "type": "Software", "parent_id": 27},
    {"id": 189, "name": "Web Security Tools", "type": "Software", "parent_id": 27},
    {"id": 190, "name": "Email Security Tools", "type": "Software", "parent_id": 27},
    {"id": 191, "name": "Identity and Access Management Tools", "type": "Software", "parent_id": 27},
    {"id": 192, "name": "Security Information and Event Management Tools", "type": "Software", "parent_id": 27},
    {"id": 193, "name": "Intrusion Detection Systems", "type": "Software", "parent_id": 27},
    {"id": 194, "name": "Intrusion Prevention Systems", "type": "Software", "parent_id": 27},
    {"id": 195, "name": "Endpoint Detection and Response Tools", "type": "Software", "parent_id": 27},
    {"id": 196, "name": "Security Orchestration, Automation, and Response Tools", "type": "Software", "parent_id": 27},
    {"id": 197, "name": "Threat Intelligence Platforms", "type": "Software", "parent_id": 27},
    {"id": 198, "name": "Vulnerability Management Tools", "type": "Software", "parent_id": 27},
    {"id": 199, "name": "Penetration Testing Tools", "type": "Software", "parent_id": 27},
    {"id": 200, "name": "Forensic Analysis Tools", "type": "Software", "parent_id": 27},
]


def get_category_by_id(category_id):
    for category in categories:
        if category["id"] == category_id:
            return category["name"]
    return None


countries = [
    {"id": 1, "name": "Somalia"},
    {"id": 2, "name": "United States"},
    {"id": 3, "name": "United Kingdom"},
    # Add more countries as needed
]

regions = [
    {"id": 1, "name": "Banaadir", "country": 1},
    {"id": 2, "name": "Jubaland", "country": 1},
    {"id": 3, "name": "South West", "country": 1},
    {"id": 4, "name": "Puntland", "country": 1},
    {"id": 5, "name": "Hirshabelle", "country": 1},
    {"id": 6, "name": "Galmudug", "country": 1},
    # Add more regions for Somalia
    {"id": 7, "name": "California", "country": 2},
    {"id": 8, "name": "Texas", "country": 2},
    {"id": 9, "name": "Florida", "country": 2},
    {"id": 10, "name": "New York", "country": 2},
    {"id": 11, "name": "Illinois", "country": 2},
    # Add more regions for the United States
    {"id": 12, "name": "England", "country": 3},
    {"id": 13, "name": "Scotland", "country": 3},
    {"id": 14, "name": "Wales", "country": 3},
    {"id": 15, "name": "Northern Ireland", "country": 3},
    # Add more regions for the United Kingdom
]

counties = [
    {"id": 1, "name": "Waaberi", "region": 1},
    {"id": 2, "name": "Hodan", "region": 1},
    {"id": 3, "name": "Warta Nabada", "region": 1},
    {"id": 4, "name": "Hamar Weyne", "region": 1},
    {"id": 5, "name": "Hamar Jajab", "region": 1},
    # Add more counties for Banaadir
    {"id": 6, "name": "Gedo", "region": 2},
    {"id": 7, "name": "Lower Jubba", "region": 2},
    {"id": 8, "name": "Middle Jubba", "region": 2},
    # Add more counties for Jubaland
    {"id": 9, "name": "Bay", "region": 3},
    {"id": 10, "name": "Bakool", "region": 3},
    {"id": 11, "name": "Lower Shabelle", "region": 3},
    # Add more counties for South West
    {"id": 12, "name": "San Diego County", "region": 7},
    {"id": 13, "name": "Los Angeles County", "region": 7},
    {"id": 14, "name": "Orange County", "region": 7},
    {"id": 15, "name": "Harris County", "region": 8},
    {"id": 16, "name": "Dallas County", "region": 8},
    {"id": 17, "name": "Miami-Dade County", "region": 9},
    {"id": 18, "name": "Broward County", "region": 9},
    {"id": 19, "name": "Kings County", "region": 10},
    {"id": 20, "name": "Queens County", "region": 10},
    {"id": 21, "name": "Cook County", "region": 11},
    {"id": 22, "name": "Greater London", "region": 12},
    {"id": 23, "name": "West Midlands", "region": 12},
    {"id": 24, "name": "Greater Manchester", "region": 12},
    {"id": 25, "name": "Glasgow City", "region": 13},
    {"id": 26, "name": "Edinburgh City", "region": 13},
    {"id": 27, "name": "Cardiff", "region": 14},
    {"id": 28, "name": "Swansea", "region": 14},
    {"id": 29, "name": "Belfast", "region": 15},
    # Add more counties for each region
]