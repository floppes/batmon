# batmon #

This is a set of Python scripts which use an analog-to-digital converter (ADC) to measure a battery's voltage and display a status icon on the screen. It supports the Microchip ADCs MCP3001, MCP3008 and MCP3551. These scripts are intended to be used on a Raspberry Pi running [RetroPie v4.4](https://retropie.org.uk). This project is based on [gbzbatterymonitor](https://github.com/joachimvenaas/gbzbatterymonitor).

## Installation ##

This guide will show you how to install and configure batmon. You need to login via SSH or open a terminal by pressing CTRL+ALT+F3 to enter the commands.

### Dispmanx ###

Dispmanx is used to create a layer on the screen where the battey icon is displayed. It needs to be installed first with this set of commands:

1. `cd ~`
2. `git clone https://github.com/AndrewFromMelbourne/raspidmx.git`
3. `cd raspidmx`
4. `make`
5. `sudo cp /home/pi/raspidmx/lib/libraspidmx.so.1 /usr/lib`

### batmon ###

Install batmon with these commands:

1. `cd ~`
2. `git clone https://github.com/floppes/batmon.git`
3. `cd batmon`

## Configuration ##

Run `nano config.py` to open the configuration file and adjust the settings to your needs.

## Testing ##

To test your configuration run `python main.py`. Press CTRL+C to quit.

If you are satisfied with the result, you can make the script automatically start on every boot by adding the line `python /home/pi/batmon/main.py &` (the ampersand at the end is important!) to the file `/etc/rc.local` before the line `exit 0`. You will need to be root to edit the file (`sudo nano /etc/rc.local`).