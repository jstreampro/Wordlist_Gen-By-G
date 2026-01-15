import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import os
import random
import string
from datetime import datetime
from pathlib import Path

class WordlistGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordlist_Gen By G")
        self.root.geometry("1400x900")
        
        # Dark theme colors - WhatsApp inspired green
        self.bg_dark = "#0a0a0a"
        self.bg_medium = "#1c1c1c"
        self.bg_light = "#2a2a2a"
        self.fg_color = "#25D366"
        self.fg_secondary = "#1ea952"
        self.fg_darker = "#128C7E"
        self.text_color = "#ffffff"
        self.input_bg = "#ffffff"
        self.input_fg = "#000000"
        self.input_border = "#3a3a3a"
        
        # Configure root window
        self.root.configure(bg=self.bg_dark)
        
        # Loaded wordlists storage
        self.loaded_content = []
        self.loaded_files = {}
        
        # Configure ttk styles
        self.setup_styles()
        
        # Common patterns and data for generation
        self.common_passwords = ["password", "admin", "letmein", "welcome", "monkey", 
                                "dragon", "master", "sunshine", "princess", "qwerty"]
        self.common_usernames = ["admin", "user", "test", "guest", "root", "administrator"]
        self.years = list(range(1950, 2026))
        
        # System-specific wordlists
        self.system_wordlists = {
            "linux": ["etc", "var", "usr", "bin", "sbin", "home", "root", "tmp", "opt", "proc", 
                     "sys", "dev", "boot", "lib", "passwd", "shadow", "sudoers", "ssh", "config"],
            "windows": ["Windows", "System32", "Program Files", "Users", "AppData", "ProgramData",
                       "config", "administrator", "default", "public", "temp", "downloads"],
            "IIS": ["inetpub", "wwwroot", "web.config", "aspnet", "bin", "App_Data", "logs"],
            "apache": ["www", "html", "htdocs", "httpd.conf", "apache2", "sites-available", 
                      "sites-enabled", "conf.d", "logs", "cgi-bin"],
            "ASP": ["aspx", "asmx", "ashx", "config", "web.config", "global.asax", "bin"],
            "php": ["index.php", "admin.php", "config.php", "wp-admin", "wp-content", 
                   "wp-includes", "includes", "uploads", "tmp", "phpinfo"]
        }
        
        self.setup_ui()
    
    def setup_styles(self):
        """Configure ttk styles for dark theme"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors for all widgets
        style.configure('TFrame', background=self.bg_dark)
        style.configure('TLabelframe', background=self.bg_dark, foreground=self.fg_color,
                       bordercolor=self.fg_darker, borderwidth=2, relief='solid')
        style.configure('TLabelframe.Label', background=self.bg_dark, foreground=self.fg_color,
                       font=('Arial', 10, 'bold'))
        style.configure('TLabel', background=self.bg_dark, foreground=self.text_color,
                       font=('Arial', 10))
        style.configure('TButton', background=self.bg_light, foreground=self.fg_color,
                       bordercolor=self.fg_darker, borderwidth=2, font=('Arial', 10, 'bold'),
                       relief='raised')
        style.map('TButton', background=[('active', self.fg_secondary)],
                 relief=[('pressed', 'sunken')])
        style.configure('TEntry', fieldbackground=self.input_bg, foreground=self.input_fg,
                       bordercolor=self.input_border, insertcolor=self.input_fg,
                       borderwidth=2, relief='solid')
        style.configure('TSpinbox', fieldbackground=self.input_bg, foreground=self.input_fg,
                       bordercolor=self.input_border, arrowcolor=self.fg_color,
                       borderwidth=2)
        style.configure('TCombobox', fieldbackground=self.input_bg, foreground=self.input_fg,
                       bordercolor=self.input_border, arrowcolor=self.fg_color,
                       selectbackground=self.fg_secondary, selectforeground=self.input_fg,
                       borderwidth=2)
        style.map('TCombobox', fieldbackground=[('readonly', self.input_bg)])
        style.map('TCombobox', selectbackground=[('readonly', self.input_bg)])
        
        # Notebook (tabs) styling
        style.configure('TNotebook', background=self.bg_dark, bordercolor=self.fg_darker,
                       borderwidth=2)
        style.configure('TNotebook.Tab', background=self.bg_medium, foreground=self.text_color,
                       padding=[20, 10], font=('Arial', 10, 'bold'), borderwidth=2)
        style.map('TNotebook.Tab', background=[('selected', self.bg_light)],
                 foreground=[('selected', self.fg_color)], expand=[('selected', [2, 2, 2, 0])])
    
    def setup_ui(self):
        # Main container with notebook (tabs)
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Wordlist_Gen By G", 
                               font=("Arial", 18, "bold"), foreground=self.fg_color)
        title_label.grid(row=0, column=0, pady=10)
        
        # Notebook for tabs
        notebook = ttk.Notebook(main_frame)
        notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tab 1: Password Generator
        self.password_tab = ttk.Frame(notebook, padding="10")
        notebook.add(self.password_tab, text="Password Wordlist")
        self.setup_password_tab()
        
        # Tab 2: Prefix/Suffix Generator
        self.prefix_suffix_tab = ttk.Frame(notebook, padding="10")
        notebook.add(self.prefix_suffix_tab, text="Prefix/Suffix")
        self.setup_prefix_suffix_tab()
        
        # Tab 3: System-Specific Generator
        self.system_tab = ttk.Frame(notebook, padding="10")
        notebook.add(self.system_tab, text="System-Specific")
        self.setup_system_tab()
        
        # Tab 4: Numbers Generator
        self.numbers_tab = ttk.Frame(notebook, padding="10")
        notebook.add(self.numbers_tab, text="Numbers")
        self.setup_numbers_tab()
        
        # Tab 5: File Loader
        self.file_tab = ttk.Frame(notebook, padding="10")
        notebook.add(self.file_tab, text="Load & Edit Files")
        self.setup_file_tab()
        
        # Output area at bottom
        self.setup_output_area(main_frame)
    
    def setup_password_tab(self):
        # Scrollable frame
        canvas = tk.Canvas(self.password_tab)
        scrollbar = ttk.Scrollbar(self.password_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Questionnaire fields
        ttk.Label(scrollable_frame, text="Personal Information for Password Generation:", 
                 font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        fields = [
            ("Full Name:", "name"),
            ("Profession:", "profession"),
            ("Role/Title:", "role"),
            ("Age:", "age"),
            ("Phone Number:", "phone"),
            ("Hobby:", "hobby"),
            ("Company:", "company"),
            ("Pet Name:", "pet"),
            ("Birthdate (DDMMYYYY):", "birthdate"),
            ("Favorite Team/Band:", "favorite")
        ]
        
        self.password_fields = {}
        for i, (label, key) in enumerate(fields, start=1):
            ttk.Label(scrollable_frame, text=label).grid(row=i, column=0, sticky=tk.W, pady=3)
            entry = ttk.Entry(scrollable_frame, width=40)
            entry.grid(row=i, column=1, sticky=(tk.W, tk.E), pady=3, padx=5)
            self.password_fields[key] = entry
        
        # Additional words
        ttk.Label(scrollable_frame, text="Additional Words (comma-separated):", 
                 font=("Arial", 10)).grid(row=len(fields)+1, column=0, sticky=tk.W, pady=10)
        self.additional_words = ttk.Entry(scrollable_frame, width=40)
        self.additional_words.grid(row=len(fields)+1, column=1, sticky=(tk.W, tk.E), pady=10, padx=5)
        
        # Number of passwords
        ttk.Label(scrollable_frame, text="Number of Passwords to Generate:").grid(
            row=len(fields)+2, column=0, sticky=tk.W, pady=5)
        self.password_count = ttk.Spinbox(scrollable_frame, from_=10, to=10000, width=20)
        self.password_count.set(100)
        self.password_count.grid(row=len(fields)+2, column=1, sticky=tk.W, pady=5, padx=5)
        
        # Generate button
        ttk.Button(scrollable_frame, text="Generate Password Wordlist", 
                  command=self.generate_passwords).grid(row=len(fields)+3, column=0, 
                                                        columnspan=2, pady=20)
        
        canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        self.password_tab.columnconfigure(0, weight=1)
        self.password_tab.rowconfigure(0, weight=1)
    
    def setup_prefix_suffix_tab(self):
        # Wordlist type
        ttk.Label(self.prefix_suffix_tab, text="Wordlist Type:", 
                 font=("Arial", 11, "bold")).grid(row=0, column=0, sticky=tk.W, pady=10)
        
        self.wordlist_type = ttk.Combobox(self.prefix_suffix_tab, 
                                         values=["usernames", "passwords", "emails", 
                                                "parameters", "directories", "files"],
                                         width=30, state="readonly")
        self.wordlist_type.set("usernames")
        self.wordlist_type.grid(row=0, column=1, sticky=tk.W, pady=10, padx=5)
        
        # Prefix
        ttk.Label(self.prefix_suffix_tab, text="Prefix:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.prefix_entry = ttk.Entry(self.prefix_suffix_tab, width=40)
        self.prefix_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Suffix
        ttk.Label(self.prefix_suffix_tab, text="Suffix:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.suffix_entry = ttk.Entry(self.prefix_suffix_tab, width=40)
        self.suffix_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Number of items
        ttk.Label(self.prefix_suffix_tab, text="Number of Items:").grid(row=3, column=0, 
                                                                        sticky=tk.W, pady=5)
        self.prefix_suffix_count = ttk.Spinbox(self.prefix_suffix_tab, from_=10, to=10000, width=20)
        self.prefix_suffix_count.set(100)
        self.prefix_suffix_count.grid(row=3, column=1, sticky=tk.W, pady=5, padx=5)
        
        # Generate button
        ttk.Button(self.prefix_suffix_tab, text="Generate Wordlist", 
                  command=self.generate_prefix_suffix).grid(row=4, column=0, 
                                                            columnspan=2, pady=20)
        
        self.prefix_suffix_tab.columnconfigure(1, weight=1)
    
    def setup_system_tab(self):
        ttk.Label(self.system_tab, text="Target System:", 
                 font=("Arial", 11, "bold")).grid(row=0, column=0, sticky=tk.W, pady=10)
        
        self.system_type = ttk.Combobox(self.system_tab, 
                                       values=["linux", "windows", "IIS", "apache", "ASP", "php"],
                                       width=30, state="readonly")
        self.system_type.set("linux")
        self.system_type.grid(row=0, column=1, sticky=tk.W, pady=10, padx=5)
        
        ttk.Label(self.system_tab, text="Content Type:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.system_content_type = ttk.Combobox(self.system_tab, 
                                               values=["directories", "files", "parameters", 
                                                      "configs", "mixed"],
                                               width=30, state="readonly")
        self.system_content_type.set("directories")
        self.system_content_type.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)
        
        ttk.Label(self.system_tab, text="Prefix (optional):").grid(row=2, column=0, 
                                                                   sticky=tk.W, pady=5)
        self.system_prefix = ttk.Entry(self.system_tab, width=40)
        self.system_prefix.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(self.system_tab, text="Suffix (optional):").grid(row=3, column=0, 
                                                                   sticky=tk.W, pady=5)
        self.system_suffix = ttk.Entry(self.system_tab, width=40)
        self.system_suffix.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Button(self.system_tab, text="Generate System-Specific Wordlist", 
                  command=self.generate_system_wordlist).grid(row=4, column=0, 
                                                              columnspan=2, pady=20)
        
        self.system_tab.columnconfigure(1, weight=1)
    
    def setup_numbers_tab(self):
        ttk.Label(self.numbers_tab, text="Number List Generator", 
                 font=("Arial", 12, "bold"), foreground=self.fg_color).grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=10)
        
        # Range configuration
        range_frame = ttk.LabelFrame(self.numbers_tab, text="Range Configuration", padding="10")
        range_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(range_frame, text="From:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.num_from = ttk.Entry(range_frame, width=20)
        self.num_from.insert(0, "1")
        self.num_from.grid(row=0, column=1, sticky=tk.W, pady=5, padx=5)
        
        ttk.Label(range_frame, text="To:").grid(row=0, column=2, sticky=tk.W, pady=5, padx=(20, 0))
        self.num_to = ttk.Entry(range_frame, width=20)
        self.num_to.insert(0, "1000")
        self.num_to.grid(row=0, column=3, sticky=tk.W, pady=5, padx=5)
        
        # Pattern type
        pattern_frame = ttk.LabelFrame(self.numbers_tab, text="Generation Pattern", padding="10")
        pattern_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(pattern_frame, text="Pattern Type:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.num_pattern = ttk.Combobox(pattern_frame, 
                                       values=["Sequential (1,2,3...)", 
                                              "Random Selection",
                                              "Even Numbers Only",
                                              "Odd Numbers Only",
                                              "Jump by Step",
                                              "Random in Range"],
                                       width=30, state="readonly")
        self.num_pattern.set("Sequential (1,2,3...)")
        self.num_pattern.grid(row=0, column=1, sticky=tk.W, pady=5, padx=5)
        self.num_pattern.bind("<<ComboboxSelected>>", self.on_pattern_change)
        
        # Step/Jump configuration
        ttk.Label(pattern_frame, text="Step/Jump:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.num_step = ttk.Entry(pattern_frame, width=20)
        self.num_step.insert(0, "1")
        self.num_step.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)
        self.num_step.config(state='disabled')
        
        # Count for random selection
        ttk.Label(pattern_frame, text="Count (for random):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.num_count = ttk.Entry(pattern_frame, width=20)
        self.num_count.insert(0, "100")
        self.num_count.grid(row=2, column=1, sticky=tk.W, pady=5, padx=5)
        self.num_count.config(state='disabled')
        
        # Formatting options
        format_frame = ttk.LabelFrame(self.numbers_tab, text="Formatting Options", padding="10")
        format_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(format_frame, text="Prefix:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.num_prefix = ttk.Entry(format_frame, width=20)
        self.num_prefix.grid(row=0, column=1, sticky=tk.W, pady=5, padx=5)
        
        ttk.Label(format_frame, text="Suffix:").grid(row=0, column=2, sticky=tk.W, pady=5, padx=(20, 0))
        self.num_suffix = ttk.Entry(format_frame, width=20)
        self.num_suffix.grid(row=0, column=3, sticky=tk.W, pady=5, padx=5)
        
        ttk.Label(format_frame, text="Zero Padding:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.num_padding = ttk.Combobox(format_frame, 
                                       values=["None", "2 digits (01)", "3 digits (001)", 
                                              "4 digits (0001)", "5 digits (00001)"],
                                       width=18, state="readonly")
        self.num_padding.set("None")
        self.num_padding.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)
        
        # Generate button
        ttk.Button(self.numbers_tab, text="Generate Number List", 
                  command=self.generate_numbers).grid(row=4, column=0, columnspan=2, pady=20)
        
        self.numbers_tab.columnconfigure(1, weight=1)
    
    def on_pattern_change(self, event=None):
        """Enable/disable fields based on pattern type"""
        pattern = self.num_pattern.get()
        
        if pattern == "Jump by Step":
            self.num_step.config(state='normal')
            self.num_count.config(state='disabled')
        elif pattern in ["Random Selection", "Random in Range"]:
            self.num_step.config(state='disabled')
            self.num_count.config(state='normal')
        else:
            self.num_step.config(state='disabled')
            self.num_count.config(state='disabled')
    
    def setup_file_tab(self):
        # File loading section
        file_frame = ttk.LabelFrame(self.file_tab, text="Load Wordlists", padding="10")
        file_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N), pady=5)
        
        ttk.Button(file_frame, text="Load File", command=self.load_file).grid(
            row=0, column=0, padx=5, pady=5)
        ttk.Button(file_frame, text="Load Folder (SecLists)", 
                  command=self.load_folder).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(file_frame, text="Clear All", 
                  command=self.clear_loaded).grid(row=0, column=2, padx=5, pady=5)
        
        self.loaded_label = ttk.Label(file_frame, text="No files loaded")
        self.loaded_label.grid(row=1, column=0, columnspan=3, pady=5)
        
        # File list section
        list_frame = ttk.LabelFrame(self.file_tab, text="Loaded Files", padding="10")
        list_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5, padx=(0, 5))
        
        # Listbox with scrollbar for file names
        list_scroll = ttk.Scrollbar(list_frame, orient="vertical")
        self.file_listbox = tk.Listbox(list_frame, yscrollcommand=list_scroll.set,
                                       bg=self.bg_medium, fg=self.text_color,
                                       selectbackground=self.fg_secondary,
                                       selectforeground=self.text_color,
                                       font=('Consolas', 9), height=25, width=40)
        list_scroll.config(command=self.file_listbox.yview)
        self.file_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        list_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.file_listbox.bind('<<ListboxSelect>>', self.on_file_select)
        
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Edit area
        edit_frame = ttk.LabelFrame(self.file_tab, text="Edit & View Content", padding="10")
        edit_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.edit_text = scrolledtext.ScrolledText(edit_frame, width=70, height=25,
                                                   bg=self.bg_medium, fg=self.fg_color,
                                                   insertbackground=self.fg_color,
                                                   selectbackground=self.fg_secondary,
                                                   selectforeground=self.text_color,
                                                   font=('Consolas', 10))
        self.edit_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        button_frame = ttk.Frame(edit_frame)
        button_frame.grid(row=1, column=0, pady=10)
        
        ttk.Button(button_frame, text="Copy to Output", 
                  command=self.copy_to_output).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Save Changes to Selected File", 
                  command=self.save_file_changes).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Delete Selected File", 
                  command=self.delete_selected_file).grid(row=0, column=2, padx=5)
        
        edit_frame.columnconfigure(0, weight=1)
        edit_frame.rowconfigure(0, weight=1)
        
        self.file_tab.columnconfigure(0, weight=0)
        self.file_tab.columnconfigure(1, weight=1)
        self.file_tab.rowconfigure(1, weight=1)
    
    def setup_output_area(self, parent):
        output_frame = ttk.LabelFrame(parent, text="Generated Wordlist Output", padding="10")
        output_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Larger output text area with custom colors
        self.output_text = scrolledtext.ScrolledText(output_frame, width=120, height=25,
                                                     bg=self.bg_medium, fg=self.fg_color,
                                                     insertbackground=self.fg_color,
                                                     selectbackground=self.fg_secondary,
                                                     selectforeground=self.text_color,
                                                     font=('Consolas', 10))
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        button_frame = ttk.Frame(output_frame)
        button_frame.grid(row=1, column=0, pady=10)
        
        ttk.Button(button_frame, text="Export to File", 
                  command=self.export_to_file).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Clear Output", 
                  command=self.clear_output).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Copy to Clipboard", 
                  command=self.copy_to_clipboard).grid(row=0, column=2, padx=5)
        
        self.status_label = ttk.Label(output_frame, text="Ready", foreground=self.fg_secondary,
                                     font=('Arial', 10, 'bold'))
        self.status_label.grid(row=2, column=0, pady=5)
        
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        parent.rowconfigure(2, weight=1)
    
    def generate_passwords(self):
        try:
            count = int(self.password_count.get())
            passwords = set()
            
            info = {k: v.get().strip() for k, v in self.password_fields.items()}
            additional = [w.strip() for w in self.additional_words.get().split(',') if w.strip()]
            
            base_words = []
            for value in info.values():
                if value:
                    base_words.extend(value.split())
            base_words.extend(additional)
            
            if not base_words:
                base_words = self.common_passwords.copy()
            
            special_chars_list = ['!', '@', '#', '_', '-', '.', '*', '+']
            
            while len(passwords) < count:
                if base_words and random.random() < 0.3:
                    word = random.choice(base_words)
                    num = str(random.randint(0, 9999))
                    special_char = random.choice(special_chars_list) if random.random() < 0.5 else ""
                    passwords.add(word + num + special_char)
                
                if info.get('name') and (info.get('birthdate') or info.get('phone')):
                    name = info['name'].replace(' ', '')
                    if info.get('birthdate'):
                        passwords.add(name + info['birthdate'])
                        passwords.add(name + info['birthdate'][:4])
                    if info.get('phone'):
                        passwords.add(name + info['phone'][-4:])
                
                if len(base_words) >= 2:
                    w1, w2 = random.sample(base_words, 2)
                    passwords.add(w1.capitalize() + w2 + str(random.randint(0, 99)))
                
                if base_words:
                    word = random.choice(base_words)
                    leet = word.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('s', '5')
                    passwords.add(leet + str(random.randint(0, 999)))
                
                passwords.add(''.join(random.choices(string.ascii_lowercase, k=8)) + str(random.randint(10, 99)))
                passwords.add(''.join(random.choices(string.ascii_uppercase, k=3)) + ''.join(random.choices(string.digits, k=5)))
                
                if info.get('profession') or info.get('role'):
                    prof = info.get('profession', '') or info.get('role', '')
                    passwords.add(prof + str(random.randint(2020, 2025)))
                    passwords.add(prof + str(random.randint(100, 999)))
            
            self.display_output(list(passwords)[:count])
            self.status_label.config(text=f"Generated {len(passwords)} passwords")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate passwords: {str(e)}")
    
    def generate_prefix_suffix(self):
        try:
            count = int(self.prefix_suffix_count.get())
            prefix = self.prefix_entry.get()
            suffix = self.suffix_entry.get()
            wtype = self.wordlist_type.get()
            
            wordlist = []
            
            username_bases = ["admin", "user", "test", "guest", "root", "master", "demo", "support", "help", "manager", "operator", "service"]
            common_words = ["super", "chief", "head", "main", "prime", "top", "lead", "senior", "junior", "dev", "prod", "backup"]
            
            if wtype == "usernames":
                for _ in range(count):
                    choice = random.randint(1, 6)
                    if choice == 1:
                        name = random.choice(username_bases)
                        num = random.randint(1, 9999)
                        wordlist.append(f"{prefix}{name}{num}{suffix}")
                    elif choice == 2:
                        w1 = random.choice(common_words)
                        w2 = random.choice(username_bases)
                        wordlist.append(f"{prefix}{w1}{w2}{suffix}")
                    elif choice == 3:
                        name = random.choice(username_bases)
                        year = random.randint(1990, 2025)
                        wordlist.append(f"{prefix}{name}{year}{suffix}")
                    elif choice == 4:
                        name = random.choice(username_bases)
                        wordlist.append(f"{prefix}{name}{suffix}")
                    elif choice == 5:
                        name = random.choice(username_bases)
                        sep_char = random.choice(['_', '-', '.'])
                        num = random.randint(1, 99)
                        wordlist.append(f"{prefix}{name}{sep_char}{num}{suffix}")
                    else:
                        name = random.choice(username_bases)
                        num = random.randint(100, 999)
                        wordlist.append(f"{prefix}{name}{num}{suffix}")
            
            elif wtype == "emails":
                email_names = ["john", "jane", "admin", "info", "contact", "support", "sales", "help", "service", "noreply", "team", "hello"]
                domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'company.com']
                for _ in range(count):
                    choice = random.randint(1, 4)
                    if choice == 1:
                        name = random.choice(email_names)
                        num = random.randint(1, 999)
                        domain = suffix if suffix else random.choice(domains)
                        if not domain.startswith('@'):
                            domain = '@' + domain
                        wordlist.append(f"{prefix}{name}{num}{domain}")
                    elif choice == 2:
                        name = random.choice(email_names)
                        domain = suffix if suffix else '@company.com'
                        if not domain.startswith('@'):
                            domain = '@' + domain
                        wordlist.append(f"{prefix}{name}{domain}")
                    elif choice == 3:
                        fname = random.choice(["john", "jane", "mike", "sarah", "alex"])
                        lname = random.choice(["smith", "johnson", "williams", "brown"])
                        domain = suffix if suffix else '@gmail.com'
                        if not domain.startswith('@'):
                            domain = '@' + domain
                        wordlist.append(f"{prefix}{fname}.{lname}{domain}")
                    else:
                        name = random.choice(email_names)
                        year = random.randint(85, 99)
                        domain = suffix if suffix else '@hotmail.com'
                        if not domain.startswith('@'):
                            domain = '@' + domain
                        wordlist.append(f"{prefix}{name}{year}{domain}")
            
            elif wtype == "directories":
                dirs = ["admin", "backup", "uploads", "images", "files", "docs", "data", "config", "includes", "assets", "static", "media", "temp", "cache", "public", "private", "secure", "old", "new", "test"]
                for _ in range(count):
                    if random.random() < 0.3:
                        d = random.choice(dirs) + str(random.randint(1, 99))
                    else:
                        d = random.choice(dirs)
                    wordlist.append(f"{prefix}{d}{suffix}")
            
            elif wtype == "parameters":
                params = ["id", "user", "page", "file", "name", "type", "action", "cmd", "query", "search", "key", "token", "session", "admin", "debug", "mode", "view", "edit", "delete", "update", "username", "password"]
                for _ in range(count):
                    if random.random() < 0.3:
                        p = random.choice(params) + str(random.randint(1, 9))
                    else:
                        p = random.choice(params)
                    wordlist.append(f"{prefix}{p}{suffix}")
            
            elif wtype == "files":
                files = ["index", "main", "home", "default", "config", "settings", "test", "backup", "readme", "info", "data", "db", "upload", "download"]
                exts = [".php", ".html", ".asp", ".aspx", ".txt", ".xml", ".json", ".log"]
                for _ in range(count):
                    f = random.choice(files)
                    if random.random() < 0.4:
                        f += str(random.randint(1, 99))
                    ext = random.choice(exts) if not suffix else ""
                    wordlist.append(f"{prefix}{f}{ext}{suffix}")
            
            else:
                pwd_bases = ["password", "admin", "letmein", "welcome", "master", "secret"]
                special_list = ['!', '@', '#', '_', '-', '.', '*']
                for _ in range(count):
                    base = random.choice(pwd_bases)
                    num = random.randint(1, 9999)
                    special_char = random.choice(special_list) if random.random() < 0.3 else ""
                    wordlist.append(f"{prefix}{base}{num}{special_char}{suffix}")
            
            seen = set()
            unique_list = []
            for item in wordlist:
                if item not in seen:
                    seen.add(item)
                    unique_list.append(item)
            
            self.display_output(unique_list[:count])
            self.status_label.config(text=f"Generated {len(unique_list[:count])} {wtype}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate wordlist: {str(e)}")
    
    def generate_system_wordlist(self):
        try:
            system = self.system_type.get()
            content_type = self.system_content_type.get()
            prefix = self.system_prefix.get()
            suffix = self.system_suffix.get()
            
            base_list = self.system_wordlists.get(system, [])
            wordlist = []
            
            for item in base_list:
                wordlist.append(f"{prefix}{item}{suffix}")
                
                if content_type == "files":
                    extensions = [".txt", ".conf", ".config", ".log", ".bak", ".old"]
                    for ext in extensions:
                        wordlist.append(f"{prefix}{item}{ext}{suffix}")
                
                elif content_type == "directories":
                    wordlist.append(f"{prefix}/{item}{suffix}")
                    wordlist.append(f"{prefix}{item}/{suffix}")
                
                elif content_type == "mixed":
                    wordlist.append(f"{prefix}/{item}{suffix}")
                    wordlist.append(f"{prefix}{item}.php{suffix}")
                    wordlist.append(f"{prefix}{item}.asp{suffix}")
                    wordlist.append(f"{prefix}{item}.aspx{suffix}")
            
            for item in base_list[:10]:
                for i in range(1, 6):
                    wordlist.append(f"{prefix}{item}{i}{suffix}")
            
            self.display_output(wordlist)
            self.status_label.config(text=f"Generated {len(wordlist)} {system} wordlist items")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate system wordlist: {str(e)}")
    
    def generate_numbers(self):
        try:
            num_from = int(self.num_from.get())
            num_to = int(self.num_to.get())
            pattern = self.num_pattern.get()
            prefix = self.num_prefix.get()
            suffix = self.num_suffix.get()
            padding_str = self.num_padding.get()
            
            padding = 0
            if "2 digits" in padding_str:
                padding = 2
            elif "3 digits" in padding_str:
                padding = 3
            elif "4 digits" in padding_str:
                padding = 4
            elif "5 digits" in padding_str:
                padding = 5
            
            numbers = []
            
            if pattern == "Sequential (1,2,3...)":
                numbers = list(range(num_from, num_to + 1))
            elif pattern == "Random Selection":
                count = int(self.num_count.get())
                numbers = random.sample(range(num_from, num_to + 1), min(count, num_to - num_from + 1))
            elif pattern == "Even Numbers Only":
                start = num_from if num_from % 2 == 0 else num_from + 1
                numbers = list(range(start, num_to + 1, 2))
            elif pattern == "Odd Numbers Only":
                start = num_from if num_from % 2 != 0 else num_from + 1
                numbers = list(range(start, num_to + 1, 2))
            elif pattern == "Jump by Step":
                step = int(self.num_step.get())
                numbers = list(range(num_from, num_to + 1, step))
            elif pattern == "Random in Range":
                count = int(self.num_count.get())
                numbers = [random.randint(num_from, num_to) for _ in range(count)]
            
            formatted = []
            for num in numbers:
                if padding > 0:
                    num_str = str(num).zfill(padding)
                else:
                    num_str = str(num)
                formatted.append(f"{prefix}{num_str}{suffix}")
            
            self.display_output(formatted)
            self.status_label.config(text=f"Generated {len(formatted)} numbers")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for range and count")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate numbers: {str(e)}")
    
    def load_file(self):
        filename = filedialog.askopenfilename(title="Select Wordlist File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                display_name = os.path.basename(filename)
                self.loaded_files[display_name] = {'path': filename, 'content': content}
                self.file_listbox.insert(tk.END, display_name)
                self.edit_text.delete(1.0, tk.END)
                self.edit_text.insert(1.0, content)
                self.loaded_label.config(text=f"Loaded: {display_name}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {str(e)}")
    
    def load_folder(self):
        folder = filedialog.askdirectory(title="Select SecLists Folder or Wordlist Folder")
        if folder:
            try:
                self.loaded_files.clear()
                self.file_listbox.delete(0, tk.END)
                count = 0
                
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        if file.endswith('.txt'):
                            filepath = os.path.join(root, file)
                            try:
                                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                                    content = f.read()
                                
                                rel_path = os.path.relpath(filepath, folder)
                                display_name = rel_path if len(rel_path) < 50 else "..." + rel_path[-47:]
                                
                                self.loaded_files[display_name] = {'path': filepath, 'content': content}
                                self.file_listbox.insert(tk.END, display_name)
                                count += 1
                                
                                if count >= 500:
                                    messagebox.showinfo("Info", "Loaded first 500 files. Folder contains more files.")
                                    break
                            except:
                                continue
                    
                    if count >= 500:
                        break
                
                self.loaded_label.config(text=f"Loaded {count} files from folder")
                if count > 0:
                    messagebox.showinfo("Success", f"Loaded {count} wordlist files")
                else:
                    messagebox.showwarning("Warning", "No .txt files found in selected folder")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load folder: {str(e)}")
    
    def on_file_select(self, event):
        selection = self.file_listbox.curselection()
        if selection:
            index = selection[0]
            filename = self.file_listbox.get(index)
            
            if filename in self.loaded_files:
                content = self.loaded_files[filename]['content']
                self.edit_text.delete(1.0, tk.END)
                self.edit_text.insert(1.0, content)
                self.status_label.config(text=f"Viewing: {filename}")
    
    def save_file_changes(self):
        selection = self.file_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "No file selected")
            return
        
        index = selection[0]
        filename = self.file_listbox.get(index)
        
        if filename in self.loaded_files:
            new_content = self.edit_text.get(1.0, tk.END).strip()
            self.loaded_files[filename]['content'] = new_content
            
            if messagebox.askyesno("Save to Disk", "Do you want to save changes to the original file?"):
                try:
                    filepath = self.loaded_files[filename]['path']
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    messagebox.showinfo("Success", "File saved successfully")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save file: {str(e)}")
            
            self.status_label.config(text=f"Changes saved for: {filename}")
    
    def delete_selected_file(self):
        selection = self.file_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "No file selected")
            return
        
        index = selection[0]
        filename = self.file_listbox.get(index)
        
        if messagebox.askyesno("Confirm Delete", f"Remove '{filename}' from loaded files?\n(Original file will not be deleted)"):
            if filename in self.loaded_files:
                del self.loaded_files[filename]
            self.file_listbox.delete(index)
            self.edit_text.delete(1.0, tk.END)
            self.loaded_label.config(text=f"Loaded {len(self.loaded_files)} files")
            self.status_label.config(text="File removed from list")
    
    def clear_loaded(self):
        if self.loaded_files and not messagebox.askyesno("Confirm Clear", "Clear all loaded files?"):
            return
        
        self.loaded_files.clear()
        self.file_listbox.delete(0, tk.END)
        self.loaded_content = []
        self.edit_text.delete(1.0, tk.END)
        self.loaded_label.config(text="No files loaded")
        self.status_label.config(text="All files cleared")
    
    def copy_to_output(self):
        content = self.edit_text.get(1.0, tk.END).strip()
        if content:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, content)
            self.status_label.config(text="Content copied to output")
        else:
            messagebox.showwarning("Warning", "No content to copy")
    
    def display_output(self, wordlist):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, '\n'.join(wordlist))
    
    def export_to_file(self):
        content = self.output_text.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Warning", "No content to export")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_name = f"generated_wordlist_{timestamp}.txt"
        
        filename = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name, filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                messagebox.showinfo("Success", f"Wordlist exported to:\n{filename}")
                self.status_label.config(text=f"Exported to {os.path.basename(filename)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def clear_output(self):
        self.output_text.delete(1.0, tk.END)
        self.status_label.config(text="Output cleared")
    
    def copy_to_clipboard(self):
        content = self.output_text.get(1.0, tk.END).strip()
        if content:
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
            self.status_label.config(text="Copied to clipboard")
        else:
            messagebox.showwarning("Warning", "No content to copy")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordlistGenerator(root)
    root.mainloop()