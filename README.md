# Wordlist_Gen By G

A powerful, GUI-based wordlist generator designed for authorized penetration testing and security assessments. Create customized wordlists for password attacks, username enumeration, directory fuzzing, and more.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## ⚠️ Legal Disclaimer

**This tool is intended for authorized security testing and educational purposes ONLY.** Unauthorized access to computer systems is illegal. Users are responsible for complying with all applicable laws and regulations. The author assumes no liability for misuse of this software.

## 🎯 Features

### Password Wordlist Generation
- **Personalized password lists** based on target information
- Questionnaire-based generation using:
  - Name, profession, role, age
  - Phone numbers, birthdates
  - Hobbies, company names, pet names
  - Favorite teams/bands
- Multiple generation strategies:
  - Base words + numbers + special characters
  - Leetspeak variations
  - Common password patterns
  - Profession/role-based combinations
- Generate wordlists even without input data

### Prefix/Suffix Generator
- Create wordlists with custom prefix and suffix
- Intelligent generation for:
  - **Usernames**: admin123, testuser, root2024
  - **Emails**: john.smith@company.com, admin@domain.com
  - **Parameters**: id, user, page, token, session
  - **Directories**: admin, uploads, backup, config
  - **Files**: index.php, config.xml, readme.txt
- Realistic patterns, no random gibberish

### System-Specific Wordlists
- Pre-configured wordlists for:
  - **Linux**: /etc, /var, /usr, passwd, shadow
  - **Windows**: System32, AppData, Administrator
  - **IIS**: inetpub, wwwroot, web.config
  - **Apache**: htdocs, httpd.conf, sites-available
  - **ASP**: aspx, web.config, global.asax
  - **PHP**: index.php, wp-admin, wp-content
- Multiple content types: directories, files, parameters, configs

### Number Generator
- Flexible number list generation with:
  - **Sequential**: 1, 2, 3, 4...
  - **Random Selection**: Random numbers from range
  - **Even/Odd Only**: Filter by parity
  - **Jump by Step**: Custom intervals (1, 5, 10, 15...)
  - **Random in Range**: Generate N random numbers
- Zero-padding support (01, 001, 0001)
- Custom prefix and suffix

### File Management
- **Load individual wordlist files** (.txt)
- **Load entire folders** (e.g., SecLists directory)
- View and edit loaded wordlists
- Save changes back to disk
- Click-to-view file browser interface
- Support for up to 500 files per load

### Professional Dark Theme
- WhatsApp-inspired green and dark design
- High contrast for visibility
- Professional cybersecurity aesthetic
- Fully resizable interface

## 📋 Requirements

- Python 3.7 or higher
- tkinter (usually included with Python)
- No external dependencies required!

## 🚀 Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/wordlist-gen-by-g.git
cd wordlist-gen-by-g
```

2. Run the application:
```bash
python wordlist_gen.py
```

### Building Executable

To create a standalone executable using PyInstaller:
```bash
# Install PyInstaller
pip install pyinstaller

# Build executable (Windows)
pyinstaller --onefile --windowed --name "Wordlist_Gen_By_G" wordlist_gen.py

# Build executable (Linux/macOS)
pyinstaller --onefile --windowed --name "Wordlist_Gen_By_G" wordlist_gen.py
```

The executable will be in the `dist/` folder.

## 📖 Usage

### Basic Workflow

1. **Launch the application**
2. **Select a tab** based on your needs:
   - Password Wordlist: Personal information-based passwords
   - Prefix/Suffix: Custom formatted wordlists
   - System-Specific: OS/platform-specific paths
   - Numbers: Number pattern generation
   - Load & Edit Files: Import existing wordlists

3. **Configure generation parameters**
4. **Click Generate**
5. **Export or copy** the resulting wordlist

### Example Use Cases

#### Generate Password Wordlist
```
1. Go to "Password Wordlist" tab
2. Fill in target information:
   - Name: John Smith
   - Company: TechCorp
   - Birthdate: 15081990
3. Set number of passwords: 500
4. Click "Generate Password Wordlist"
5. Export to file
```

#### Create Email List with Domain
```
1. Go to "Prefix/Suffix" tab
2. Wordlist Type: emails
3. Suffix: @company.com
4. Number of Items: 100
5. Click "Generate Wordlist"
```

#### Generate Numbered Usernames
```
1. Go to "Numbers" tab
2. From: 1000, To: 9999
3. Pattern: Sequential
4. Prefix: user
5. Zero Padding: 4 digits (0001)
6. Click "Generate Number List"
Result: user1000, user1001, user1002...
```

#### Load and Combine SecLists
```
1. Go to "Load & Edit Files" tab
2. Click "Load Folder (SecLists)"
3. Select your SecLists directory
4. Click on any file to view contents
5. Edit, combine, or copy to output
```

## 🎨 Screenshots

![Main Interface](screenshots/main_interface.png)
*Main application interface with dark theme*

![Password Generation](screenshots/password_tab.png)
*Password wordlist generation with questionnaire*

![File Browser](screenshots/file_browser.png)
*File loading and editing interface*

## 🔧 Features in Detail

### Smart Password Generation
- Combines multiple strategies for variety
- Avoids excessive repetition
- Generates realistic password patterns
- Supports both simple and complex passwords

### Prefix/Suffix Intelligence
- No random character strings
- Uses realistic base words
- Combines words meaningfully
- Proper email format handling

### Export Options
- Auto-timestamped filenames
- UTF-8 encoding support
- Direct clipboard copy
- Custom file naming

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
```bash
git clone https://github.com/yourusername/wordlist-gen-by-g.git
cd wordlist-gen-by-g
# Make your changes
# Test thoroughly
# Submit PR
```

## 📝 Todo / Roadmap

- [ ] Add more system-specific wordlists (Nginx, Tomcat, etc.)
- [ ] Implement wordlist combination modes
- [ ] Add character set customization
- [ ] Export to multiple formats (JSON, CSV)
- [ ] Add wordlist statistics and analysis
- [ ] Implement mutation rules engine
- [ ] Add keyboard walk patterns

## 🐛 Known Issues

- Large folder loads (1000+ files) may take time
- Very large wordlists (100k+ items) may slow down the UI

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**G**
- GitHub: [@jstreampro)

## 🙏 Acknowledgments

- Inspired by various wordlist generation tools in the security community
- Built for the penetration testing and ethical hacking community
- Thanks to all contributors and testers

## 💡 Tips for Effective Wordlist Generation

1. **Know your target**: The more information you have, the better your wordlists
2. **Combine multiple sources**: Use password + numbers + system-specific lists
3. **Test incrementally**: Start with smaller wordlists and expand
4. **Consider context**: Different targets need different approaches
5. **Stay legal**: Always have written authorization before testing

## 🔒 Security Notice

This tool generates wordlists that may be used in security testing. Store generated wordlists securely and delete them when no longer needed. Never share wordlists that contain real user information.

---

**⚖️ Use Responsibly | 🎯 Test Ethically | 🔐 Stay Legal**
