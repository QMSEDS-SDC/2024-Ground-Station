# 2024-GUI-Ground

## General Design

The GUI will allow the user to interact with the CubeSat and also logging of data that are provided by the CubeSat. The functionality can be summarised as:

- Phase 1
  - Shows Status of comms link and *potentially troubleshoot simple issues*
  - Command cubesat to perform a detailed healthcheck, display that data to an user and log the data.
- Phase 2
  - Initiate the stage and provide the cubesat with number series that it should look for
  - Provide image updates to showcase the identification results of the cubesat and also *provide a way to overide the automatic detection*
- Phase 3
  - Initiate this stage and its sub-phases *unless that is meant to be done automatically*
  - Display some image frames to ensure the dock detection is done properly and to check alighment. *Also allow retrying of this step*
  - For sub-phase 2, displays and stores images so that the user can manually identify and access the damages.
  - For sub-phase 3, *maybe live feed*.

## Design Inspiration

The inspiration of the design was taken from Proxmox's Interface. Though the usecases are different, the core purpose is the same - to manage systems.

![alt text](./img_src/image.png)