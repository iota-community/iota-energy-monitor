# IOTA Energy Monitor

![IOTA Energy Monitor](https://i.imgur.com/I3KxeM9.png)

The IOTA Energy Monitor is a hardware and software project that is designed to take power and meter readings over Modbus and via CT Clamps. The device is also equipped with a CryptoCore module to enable it to issue IOTA transactions and manage funds securely. 

This repo is split into two parts:

### /hardware

This portion of the repo contains the design files for the IOTA Energy Monitor. The device was designed in EAGLE by Autodesk. 

The repo contains the lasted Gerber files in a .zip for easy reproduction.

### /software

This folder contains the micropython software for the energy meter. In order to flash it you should use the Pymakr extension of VSCode.

##### License

Apache 2.0 