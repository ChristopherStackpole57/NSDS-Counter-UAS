# System Architecture

## Prerequisites

This project conforms to [MISRA C++](https://misra.org.uk/misra-cpp2023-released-including-hardcopy/) and
[MOSA](https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf) standards.

## System Overview

### CV

the cv system

### LiDAR

the lidar system

### Fusion

the fusion system

### GNC

The Guidance, Navigation, and Controls (GNC) system is responsible for processing target packages aggregated by the fusion system and aligning the sentry with the optimal
target. GNC is made up of sub systems for each responsibility (Guidance vs Navigation vs Controls) and acts as middleware between the identification and decision making 
sections of the turret software, and the pan-tilt hardware responsible for orienting the turret.

GNC also handles target tracking and prediction, by estimating target positions and comparing estimations with measurements through a Kalman filter. To ensure internal state
accuracy, GNC makes use of feedback control logic to validate turret alignment.

[GNC System Documentation](cpp_code/gnc/documentation/README.md)