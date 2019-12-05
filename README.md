# AirSimControl
* AirSimControl.py
* Greg McIntyre
  
Built from AirSimClient behaviours. A console and graphical interface for using pyclient to contol AirSim multirotor.   
TODO: Relative to Absolute Position of drones  
NOTE: Redundant files have been left in place for future improvement  

# AirSim Setup
https://microsoft.github.io/AirSim/docs/build_windows/

# AirSimControl Setup
https://github.com/gregorymcintyre/AirSimControl.git
* Extract/copy files to
\Documents\Unreal Projects\AirSimDev\Plugins\AirSim\AirSimControl

* copy settings.json to
\Documents\AirSim

* Run AirSimControl with
python AirSimContol.py

# Command Key
* `<ID>` = Drone Identifier e.g. ALPHA (found in settings.json)
* `<CMD>` = Command e.g. land
* `<CS>` = Callsign e.g. YEET (found in callsigns.txt)
* `<T>` = Travel time
* `<S>` = Speed e.g. 5
* `<X> <Y> <Z>` = Cartesian locations e.g. -10 10 -10 NOTE: `<Z>` is inverted
* `<POLAR> <ALPHA>` = Angular directions from location

# `<CMD>`
* land = perform land proceedure
  * `<ID> <CMD>`
* move_to = move to gird 
  * `<ID> <CMD> <CS>`
  * `<ID> <CMD> <CS> <S>`
  * `<ID> <CMD> <X> <Y> <Z>`
  * `<ID> <CMD> <X> <Y> <Z> <S>`
* move_direction = move in direction
  * `<ID> <CMD> <POLAR> <ALPHA>`
  * `<ID> <CMD> <POLAR> <ALPHA> <S | R>`
* takeoff = take off proceedure
  * `<ID> <CMD>`
* quit = quit AirSimControl

# Unlisted test commands
These commands are issued without any other identifiers and are used to control the intial 5 drones.
* getup = all drones takeoff
  * `<CMD>`
* getdown = all drones land
  * `<CMD>`
* starburst = all drones move outward 10 units at speed 5
  * `<CMD>`
* converge = all drones return to intial Origin at speed 1
  * `<CMD>`
