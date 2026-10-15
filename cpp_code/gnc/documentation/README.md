# Guidance, Navigation, and Controls

## Overview

The Guidance, Navigation, and Controls system is a middleware system that processes target packages from the fusion system, and issues commands to the pan-tilt system
to align the turret with a determined target vector. GNC is split into four primary components:
- GNCEngine
- GuidanceEngine
- NavigationEngine
- ControlsEngine

GNCEngine is the primary orchestrator for GNC, and owns the other engines. GNCEngine iteracts with earlier systems by receiving and configuring target packages, before
dispatching further processing calls in the other engines.

## Guidance

The GuidanceEngine is responsible for processing the target packages configured by GNCEngine, and determining where the turret should aim.

The GudianceEngine operates in several key phases:
- Target Statevector Assimilation using Kalman filters.
- Optimal Target Selection.
- Ballistic Effects Simulation.
- Target Statevector Output.

### Target Statevector Assimilation

In any mechanical or electronic system there will be measurement uncertainty. To minimize the effects of measurement uncertainty, the GuidanceEngine uses Kalman filters to
predict target locations. Because predicted locations may differ from measured locations, and both have uncertainty associated with them, the Kalman Filter approach balances
both locations to determine the most likely position of the target.

### Optimal Target Selection

When a list of targets is available to the GuidanceEngine, a decision must be made for which target to align to. The optimal target selection phase looks at several factors
such as the turrets current orientation, a prospective targets' position, target confidence, available elimination methods, and target size (Class 1 vs Class 2 UAS, etc.).
Optimal Target Selection requires a careful balance of its input properties to ensure that targets are eliminated in an effective, efficient manner, and that chosen targets
actually enemies.

### Ballistic Effects Simulation

Kinetic elimination methods, at any engagement distance, will experience interference from the environment. When a target has been chosen, the GuidanceEngine must account for 
what interference the kinetic elimination method will experience, based on properties of the elimination method. These properties may include things such as muzzle velocity,
drag coefficients, lead angles, and gravitational effects.

### Target Statevector Output

Once a target has been chosen, its location has been processed, and a ballistics offset has been calculated, the GuidanceEngine returns the target statevector to the GNCEngine
for processing by other subsystems.

## Navigation

The NavigationEngine is responsible for determining the current statevector of the turret.

NOTE: this subsytem is still being researched.

## Controls

The ControlsEngine is responsible for dispatching commands to the turret hardware to align the turret with the target statevector. To determine the necessary commands, the
ControlsEngine receives the target statevector and the current statevector, and uses a PID loop to determine an errror-corrected amount of rotation to apply. The ControlsEngine
operatres in three key phases:
- Rotation Calculation.
- Error Correction.
- Command Issuance.

### Rotation Calculation

Using the difference between the target statevector and the current statevector, the ControlsEngine calculates the necessary rotation along each of the principle axes.

### Error Correction

To account for small errors in the pan-tilt system's rotation, a Proportional-Integral-Derivative loop is used to have error from previous commands inform the calculated
rotation for future commands. As the system runs error correction becomes increasingly accurate as the exact error of the hardware is observed.

### Command Issuance

Once error-corrected rotations have been calcualated, the ControlsEngine generates commands for the pan-tilt hardware and issues them via serial bus.

Commands and issuance techniques are specific to the hardware in use. The currently selected hardware is the Directed Perception PTU-46-17.5 Pan-Tilt Unit, and commands are
issued via serial bus connection. Different hardware backends will require different command issuance code.