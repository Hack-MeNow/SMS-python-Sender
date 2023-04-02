
#!/bin/bash

# Function to display help information
show_help() {
    echo "Usage: installer.sh [OPTION]"
    echo "Install or run the SMS Sender tool."
    echo ""
    echo "Options:"
    echo "  -i, --install       Install Python and required packages"
    echo "  -r, --run           Run the SMS Sender tool"
    echo "  -h, --help          Display this help message"
    exit 0
}

# Function to install Python and required packages
install() {
    # Download and extract Python
    curl -O https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz
    tar -zxvf Python-3.10.2.tgz

    # Install Python
    cd Python-3.10.2
    ./configure --enable-optimizations
    make -j$(nproc)
    sudo make altinstall

    # Install pip
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3.10 get-pip.py --user

    # Install required packages from requirements.txt
    pip3.10 install -r requirements.txt

    # Verify installation
    python3.10 --version
    pip3.10 --version

    echo "Python and required packages installed successfully."
}

# Function to run the SMS Sender tool
run() {
    # Check if Python is installed
    if ! command -v python3.10 &> /dev/null; then
        echo "Python is not installed. Please run the installer with the -i option to install Python and required packages."
        exit 1
    fi

    # Run the SMS Sender tool
    python3.10 Sms_sender.py
}

# Parse command line options
while [[ $# -gt 0 ]]; do
    key="$1"

    case $key in
        -i|--install)
            install
            shift
            ;;
        -r|--run)
            run
            shift
            ;;
        -h|--help)
            show_help
            shift
            ;;
        *)
            echo "Invalid option: $key"
            show_help
            shift
            ;;
    esac
done

# If no options are provided, display help information
if [[ $# -eq 0 ]]; then
    show_help
fi
