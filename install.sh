
sudo apt-get update && apt-get upgrade -y
echo "====================================="
echo " [+] System updated successfully"
echo "====================================="
sleep 5
clear
sleep 2

echo " [?] Installing unzip..."
echo " [?] Installing wget...\n\n"
sleep 3
clear
sudo apt-get install wget && sudo apt-get install unzip && sudo apt-get install tar
sleep 1
echo "[+] WGET Successfully installed!"
sleep 1
echo "[+] UNZIP Successfully installed!"
sleep 1
echo "[+] TAR Successfully installed!"
sleep 4
clear
sleep 2

echo "============== + Choose a browser emulator + =============="
echo "[1] - Windows"
echo "[2] - Firefox"
echo "==========================================================="

read -p "Choose an option: " value

if [ $value == "1" ]; then
    echo "Downloading chromedriver...\n\n"
    sleep 2
    wget https://chromedriver.storage.googleapis.com/102.0.5005.27/chromedriver_linux64.zip

    vini=`ls | grep chromedriver_linux64.zip`
    if [ $? == 0 ]; then
        clear
        echo "Chromedriver successfully downloaded!"
        echo $vini
        sleep 2
        clear
        echo "Extracting file..."
        sleep 2
        unzip chromedriver_linux64.zip
        rm -rf chromedriver_linux64.zip

        qq=`ls | grep chromedriver`
        if [ $? == 0 ]; then
            clear
            echo "File extracted successfully!"
            sleep 1
        else
            clear
            echo "Unexpected error extracting the file"
            exit
        fi

    else
        echo "[!] Download error!"
        exit
    fi

elif [ $value == "2" ]; then
    echo "Downloading geckodriver"
    sleep 2
    wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
    
    vini=`ls | grep geckodriver-v0.31.0-linux64.tar.gz`
    if [ $? == 0 ]; then
        clear
        echo "Geckodriver successfully downloaded!"
        echo $vini
        sleep 2
        clear
        echo "Extracting file..."
        sleep 2
        tar -vzxf geckodriver-v0.31.0-linux64.tar.gz
        rm -rf geckodriver-v0.31.0-linux64.tar.gz
 
        qq=`ls | grep geckodriver`
        if [ $? == 0 ]; then
            clear
            echo "File extracted successfully!"
            sleep 1
        else
            clear
            echo "Unexpected error extracting the file"
            exit
        fi
    else
        echo "[!] Download error!"
        exit
    fi
fi
