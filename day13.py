initial_state = """                          /------------------------------\\                                           /----------\\
                          |             /----------------+----------------------------------------\\  |          |
                          |             |                |                                    /---+--+----------+-------------------------------\\
                          |             |        /-------+------------------------------------+---+--+----------+-----------------------------\\ |
                          |             |        | /-----+-----------------------------\\/-----+---+--+----------+--------\\                    | |
    /-------------->\\     |             |        | |     |                             ||     |   |  |   /------+--------+--------------------+\\|
    |               |     |             |   /----+-+-----+---------------\\             ||     |   |  |   |      |        |                    |||
    |    /----------+-----+\\  /---------+---+----+-+-----+---------------+---------\\   ||/----+---+\\ |   |      |        |                    |||
/---+----+----------+-----++--+----\\    |   |    | |     |           /---+----\\ /--+---+++----+---++-+---+-->->-+--------+--\\                 |||
|   |    |          |    /++--+----+----+---+----+-+-----+-----------+---+----+-+--+---+++----+---++-+---+------+--\\     |  |                 |||
|   |/---+----------+----+++--+----+--\\ |   |    | |     |           |   |    | |  |   |||    |   || \\---+------/  |     |  |                 |||
|   ||   |          |    |||  |    |  |/+---+----+-+-----+-----------+--\\|    | |  |   |||    |   ||     |         |     |  |          /------+++----\\
|   ||   |     /----+----+++--+----+--+++---+----+-+-----+-----------+--++----+-+--+---+++----+---++-----+-------\\ |     |  |          |      |||    |
|   ||   |/----+----+----+++--+----+--+++---+----+-+-----+-----------+--++-\\  | |  |   |||/---+---++-----+--\\    | |     | /+---------\\|      |||    |
|   ||   ||    |    |    |||  |  /-+--+++---+----+-+-\\   |/----------+--++-+--+-+--+---++++---+---++-----+--+----+-+-----+-++\\        ||      |||    |
|   ||   ||  /-+----+----+++--+--+-+--+++---+----+-+-+---++----\\  /--+--++-+--+-+--+---++++---+<--++-----+--+----+-+-----+-+++-------\\||      |||    |
|   ||   ||  | |    |    ||| /+--+-+--+++---+----+-+-+---++----+--+--+--++-+--+-+--+---++++---+---++-----+--+----+-+-<---+-+++---\\ /-+++------+++\\   |
|   ||   ||  | |    |    ||| ||  | |  |||   |    | | |   ||    |  | /+--++-+--+-+--+---++++---+\\  ||     \\--+----+-+-----+-+++---+-+-+++------+/||   |
|   ||   ||  | |    |    ||| ||  | |  |||   |    | | |   ||    |  | ||  || |  |/+--+---++++---++--++---\\    |    | |     | |||   | | |||      | ||   |
|   ||/--++--+-+----+----+++-++--+-+--+++---+----+-+-+---++----+--+-++--++-+--+++--+\\  ||||   ||  ||   |    |    | |     | |||   | | |||      | ||   |
|   |||  ||  | |    |    ||| ||  | | /+++---+----+-+-+---++----+--+-++--++-+--+++--++--++++---++--++---+----+----+-+---\\ | |||   | | |||      | ||   |
|   |||  ||  | |    |    ||| ||  | | ||||   |    | | |   ||    |  | ||  || |  |||  || /++++---++--++---+----+----+-+---+-+-+++---+-+-+++----\\ | ||   |
|   |||  ||  | |    |    ||| ||  | | |||\\---+----+-+-+-->++----+--+-++--++-+--+++--++-+++++---++--/|   |    |    | |   | | |||   | | |||    | | ||   |
|   |||  ||  | |    |    ||| ||  | | |||    |    | | |   ||    |  | || /++-+--+++--++-+++++---++---+---+----+----+-+---+-+-+++---+\\| |||    | | ||   |
|   |||  ||  \\-+----+----+++-++--+-+-+++----+----+-+-+---++----/  | || ||| |  |||  || |||||   ||   |   |    |    | |   | | |||   ||| |||    | | ||   |
|   |||  || /--+----+----+++-++--+-+-+++----+--\\ | | |   ||/------+-++-+++-+--+++--++-+++++---++---+---+----+----+-+-\\ | | |||   ||| |||    | | ||   |
|  /+++--++-+--+----+----+++-++--+-+-+++----+--+-+-+-+---+++------+-++-+++-+--+++--++\\|||||   ||   |   |    |    | | | | | |||   ||| |||    | | ||   |
|  ||||  || | /+----+----+++-++--+-+-+++----+--+-+-+-+---+++------+-++-+++-+--+++--++++++++---++---+---+----+----+-+-+-+-+\\|||   ||| |||    | | ||   |
|  ||\\+--++-+-++----+----+++-++--+-+-+/|    |  | | | |   |||      |/++-+++-+--+++--++++++++---++---+---+----+\\   | | | | |||||   ||| |||    | | ||   |
|  || |  || | || /--+--<-+++-++--+-+-+-+----+--+-+-+-+---+++------++++-+++-+--+++--++++++++---++---+--\\|    ||   | | | | |||||   ||| |||    | | ||   |
| /++-+--++-+-++-+--+----+++-++--+-+-+-+----+--+-+-+\\|   |||    /-++++-+++-+--+++--++++++++---++---+--++---\\||   | | | | |||||   ||| |||    | | ||   |
| ||| |  || | || |  |    ||| ||  | | | |    |  | | |||   |||/---+-++++-+++-+--+++--++++++++---++-\\ |  ||   |||   | | | | |||||   ||| |||    | | ||   |
| ||| |  || |/++-+--+----+++-++--+-+-+-+----+--+-+-+++---++++---+-++++-+++-+--+++\\ |||||||\\---++-+-+--++---+/|   | | | | |||||   ||| |||    | | ||   |
| ||| |  || |||| |  |    ||| ||  | | |/+----+--+-+-+++---++++---+-++++-+++-+--++++-+++++++----++-+-+--++---+-+---+-+-+-+-+++++\\  ||| |||    | | ||   |
| ||| |  || |||| |  |    ||| ||  | | |||    |  | | |||   ||||   | |||| ||| |  |||| |||||||    || | |  ||   | |   | | | | ||||||  ||| |||    | | ||   |
| ||| |  || |||| |  |    |\\+>++--+-+-+++----+--+-+-+++---/|||   | |||| ||| |  |||| |||||||    || | |  ||   | |   | | | | ||||||  ||| |||    | | ||   |
| ||| |  || |||| |  |   /+-+-++--+-+-+++----+--+-+-+++--\\ |||   | |||| ||| |  |||| |||||||    || | |/-++---+-+---+-+-+-+-++++++--+++-+++---\\| | ||   |
| ||| |  || ||||/+--+---++-+-++--+\\| ||\\----+--+-+-+++--+-+++---+-++++-+/| |  |||| |||||||    || | || ||   | |   | | | | ||||||  ||| |||   || | ||   |
| ||| |  \\+-++++++->+---++-/ ||  \\++-++-----+--+-+-++/  | |||   | |||| | | |  |||| |||||||    || |/++-++---+-+---+-+-+-+-++++++--+++-+++\\  || | ||   |
| ||| |   | ||||||/-+---++---++---++-++-----+--+-+-++---+-+++---+-++++-+-+-+-\\|||| |||||||    || |||| ||   | |   | | | | ||||||  ||| ||||  || | ||   |
| ||| |   | ||||||| |   ||   ||   || || /---+--+-+-++---+-+++---+-++++-+-+-+-+++++-+++++++----++-++++-++---+-+\\  | | | | ||||||  ||| ||||  || | ||   |
| ||| |   | ||||||| |   ||   ||   || || |   |  | | ||   |/+++---+-++++-+-+-+\\||||| |||||||    || |||| ||   | ||  | | | | ||||||  ||\\-++++--++-+-+/   |
| ||| |   | ||||||| |   ||   ||   || || |   |  | | ||   |||||/--+-++++-+-+-+++++++-+++++++----++-++++-++---+-++--+-+-+-+-++++++--++\\ ||||  || | |    |
| ||| |   | ||||||| |   ||   ||   || || |   |  | | ||  /++++++--+-++++-+-+-+++++++-+++++++----++-++++-++---+-++--+-+-+-+-++++++--+++-++++\\ || | |    |
| ||| |   | ||||||| |   ||   \\+---++-++-+---+--+-+-++--+++++++--+-++++-+-+-+++++++-+++++++----++-++++-++---+-++--+-+-+-+-++++++--/|| ||||| || | |    |
| ||| |   | ||||||| |   ||  /-+---++-++-+---+--+-+-++--+++++++--+-++++-+-+-+++++++-+++++++----++-++++-++---+-++--+-+-+\\| ||||||   || ||||| || | |    |
| ||| |   | ||||||| |   ||  | |   || || |   |  | | ||  |||||||  | |||| | | ||||||| |||||||    || |||| ||   | ||  | | ||| ||||||   || ||||| || | |    |
| ||| |   | ||||||| |   ||  | |   || || |   |  | | ||  |||||||  | |||| | | ||||||| |||||||    || ||||/++---+-++--+-+-+++>++++++---++-+++++-++-+\\|    |
\\-+++-+---+-+++++++-+---++--+-+---+/ || |   |  | | \\+--+++++++--+-++++-+-+-+++++++-++++/||    || |||||||   | ||  | | ||| ||||||   || ||^|| || |||    |
  ||| |   | ||||||| |   || /+-+---+--++-+---+--+-+--+--+++++++-\\| |||| | | ||||||| |||| ||    || |||||||   | ||  | | ||| ||\\+++---++-+/||| || |||    |
  ||| |   | ||||||| |   || || |   |  || |   |  | |  |  ||||||| || |||\\-+-+-+++/||| |||| ||    || |||||||   | ||  | | ||| || |||   || | ||| || |||    |
  ||| |   | ||||||| |   || || |   |  || |   |  | |  |  ||||||| || |||  | | ||| ||| |||| ||/---++-+++++++---+-++-\\| | ||| || |||   || | ||| || |||    |
  ||| |   | ||||||| |   ||/++-+---+--++-+---+--+-+--+--+++++++-++-+++--+-+-+++-+++-++++-+++---++-+++++++---+-++-++-+-+++-++-+++\\  || | ||| || |||    |
  ||| |   | ||||||| |   |\\+++-+---+--++-+---+--+-+--+--+++++++-++-+++--+-+-+++-+++-++++-+++---++-+++++++---+-++-++-/ ||| || ||||  || | ||| || |||    |
  \\++-+---+-+++++++-+---+-+++-+---+--++-+---+--+-+--/  ||||\\++-++-+++--+-+-+++-+++-++++-+++---++-+++++++---+-++-++---/|| || ||||  || |/+++-++-+++---\\|
   || |   | ||||||| |   | ||| | /-+--++-+---+--+-+-----++++-++-++-+++--+-+-+++-+++-++++-+++---++-+++++++---+-++-++----++-++-++++--++-+++++\\|| |||   ||
   || |   \\-+++++++-+---+-+++-+-+-+--++-+---+--+-+-----++++-++-++-+++--+-+-/|| ||| |||| \\++---++-+++++++---+-++-++----++-/| ||||  || |||||||| |||   ||
   || |     ||||||| | /-+-+++-+-+-+--++-+-\\ |/-+-+-----++++-++\\|| |||  | |  || \\++-++++--++---++-++++++/   | || ||    ||  | ||||  || |||||||| |||   ||
   || |     |||||\\+-+-+-+-+++-+-+-+--++-+-+-++-+-+-----++++-+++++-+++--+-+--++--++-++++--++---++-+++++/   /+-++-++-\\  ||  | ||||  || |||||||| |||   ||
   || |     ||||| | | | | ||| | | |  || | | || | |     |||| ||||| |||  | |/-++--++-++++--++---++-+++++----++-++-++-+--++--+-++++--++-++++++++\\|||   ||
  /++-+-----+++++-+-+-+-+-+++-+-+-+--++-+-+-++-+-+-----++++-+++++-+++--+-++-++--++-++++--++---++-+++++--\\ || || || |  ||  | ||||  || ||||||||||||   ||
  ||| |     ||||| | | | | ||| | | |  || | | || | |     |||| ||||| |||  | || ||  || ||||  ||   || |||||  | || || || |  ||  | ||||  || ||||||||||||   ||
  ||| |    /+++++-+-+-+-+-+++-+-+-+--++-+-+-++-+-+-----++++-+++++-+++--+-++-++\\ || ||||  ||   || |||||  | || || || |  ||  | ||||  || ||||||||||||   ||
  ||\\-+----++++++-+-/ | | ||| | | |  |\\-+-+-++-+-+-----++++-+++++-+++--+-++-+++-++-++++--++---++-+++++--+-++-++-++-+--++--+-++/|  || ||||||||||||   ||
  ||  |    |||||| |   | | ||| | | |  |  |/+-++-+-+----\\|||| ||||| ||\\--+-++-+++-++-++++--++---+/ ||||\\--+-++-++-++-+--++--+-++-+--++-++++++++++/|   ||
  ||/-+----++++++-+---+-+-+++-+-+-+--+--+++-++\\| |    |||||/+++++-++---+-++-+++-++-++++--++---+--++++---+-++-++-++-+--++--+-++-+--++\\|||||||||| |   ||
  ||| |    |||||| |   | | ||| | | |  |  ||| |||| |    ||||||||||| ||   | || ||| || ||||  ||   |  ||||   | || || || |  ||  | || |  ||||||||||||| |   ||
  ||| |    |||||| |   | | |||/+-+-+--+--+++-++++-+----+++++++++++-++---+-++-+++-++-++++--++---+--++++---+-++-++-++-+\\ ||  | || |  ||||||||||||| |   ||
  ||| | /--++++++-+---+-+-+++++-+-+--+--+++-++++-+----+++++++++++-++---+-++-+++-++-++++--++---+--++++---+-++\\|| || || ||  | || |  ||||||||||||| |   ||
  ||| | |/-++++++-+---+-+-+++++-+-+--+-\\||| |||| |    ||||||||||| ||   | || ||| || ||||  ||   |  ||||   | ||||| || || ||  | || |  ||||||||||||| |   ||
  ||| | || |||||| |   | | ||||| \\-+--+-++++-++++-+----+++++++++++-++---+-++-+++-++-++++--++---+--++++---+-+++++-++-++-++--+-++-+--++++++++/|||| |   ||
  ||| | || |||||| |   | | ||||\\---+--+-++++-++++-+----+++++++++++-++---+-++-+++-++-/|||  ||   |  ||||   | ||||| || || ||  | || |  |||||||| |||| |   ||
/-+++-+-++-++++++-+---+-+-++++----+--+-++++-++++-+-\\/-+++++++++++-++---+-++-+++-++--+++--++---+\\ ||||   | ||||| || || ||  | || |  |||||||| |||| |   ||
| ||| | || |||||| |   | | ||||    |  | |||| |||| | || ||||||\\++++-++---+-++-+++-++--+++--++---++-/|||   | ||||| || || ||  | || |  |||||||| |||| |   ||
| ||| | || |||||| |   | | ||||    |  | |||| |||| | || |||||| |||| ||  /+-++-+++-++--+++--++---++--+++---+-+++++-++-++-++--+-++-+--++++++++-++++-+\\  ||
| ||| | || |||||| |   | | ||||    |  | |||| |||| \\-++-++++++-++++-++--++-++-+++-++--+++--++---++--+++---+-+++++-++-++-++--+-++-+--++++++++-+++/ ||  ||
| ||| | || |||||| |   | |/++++----+--+-++++-++++---++-++++++-++++-++--++-++-+++-++--+++--++-\\ ||  |||   | ||||| || || ||  | || |  |||||||| |||  ||  ||
| ||| | || |||||| |   | ||||||    |  | |||| ||||   || |||||| |||| ||  || || ||| ||  |||  || | ||  |||   | ||||| || || ||  | || |  |||||||| |||  ||  ||
| ||| | ||/++++++-+--\\| ||||||    |  | |||| ||||   || |||||| |||| ||  || || ||| ||  |||  \\+-+-++--+/\\---+-+++++-++-++-++--+-++-+--++++++++-/||  ||  ||
|/+++-+-+++++++++-+--++-++++++\\   |  | |||| ||||   || |||||| |||| ||  |\\-++-+++-++--+++---+-+-++--+-----+-+++++-++-++-++--+-++-+--/|||||||  ||  ||  ||
||||| | ||||||||| |  || |||||||   |  | |||| ||||   || |||||| |||| ||  |  || ||| ||  |||   | | ||  |     | ||||| || || ||  | || |   |||||||  ||  ||  ||
||||| | ||||||||| |  || |||||||   |  | |||| ||||   || |||||| |||| ||  |  || ||| ||  |||   | | ||  |     | ||||| || || ||  | || |   |||||||  ||  ||  ||
||||| | ||||||||| |  || |||||||   |  | |||| ||||   || |||||| |||\\-++--+--++-+++-++--+++---+-+-++--+-----+-+/||| || || ||  | || |   |||\\+++--++--++--/|
||||| | ||||||||| |  || |||||||   |  | |||| ||||   || |||||| |||  ||  |  || ||| ||  |||   | | ||  |     | | ||| || || ||  | || |   ||| |||  ||  ||   |
||||\\-+-+++++++++-+--++-+++++++---+--+-++++-++/|/--++-++++++-+++--++--+--++-+++-++--+++---+-+-++--+-----+-+-+++-++-++-++\\ | || |   ||| |||  ||  ||   |
||||  | ||||||||| |  || |||||||   |  | |||| || ||  || |||||| |||  ||  |  || ||| \\+--+++---+-+-++--+-----+-+-+++-++-++-+++-+-/| |   ||| |||  ||  ||   |
||||  | ||||||||| |  || |||||||/--+--+-++++-++-++--++-++++++-+++--++--+--++-+++--+--+++---+-+-++--+-----+-+-+++\\|| || ||| |  | |   ||| |||  ||  ||   |
||||  | ||||||||| |  ||/++++++++--+--+-++++-++-++--++-++++++-+++--++--+--++-+++--+--+++---+-+-++--+-----+\\| |||||| || ||| |  | |   ||| |||  ||  ||   |
||||  | |||\\+++++-+--+++++++++++--+--+-++++-++-++--++-++++++-+++--++--+--++-++/  |  |||   | | ||  |     ||| |||||| || ||| |  | |   ||| |||  ||  ||   |
||||  | ||| ||||| |  |||\\+++++++--+--+-++++-++-++--++-++/||\\-+++--++--+--++-++---+--+++---+-+-++--+-----+++-++++++-++-+++-+--+-+---+/| |||  ||  ||   |
||||  |/+++-+++++-+--+++-+++++++--+--+-++++-++-++--++-++-++--+++--++--+--++-++---+--+++---+-+-++--+---\\ ||| |||||| || ||| |  | |   | | |||  ||  ||   |
||||  ||||| ||||| |  ||| |||||||  |  | |||| || ||  || ||/++--+++--++--+--++-++---+--+++---+-+-++--+---+-+++-++++++-++-+++-+--+-+---+-+-+++--++--++-\\ |
||||  ||||| \\++++-+--+++-+++++++--+--+-++++-++-/|  || |||||  |||  ||  |  || ||   |  |||   | | \\+--+---+-+++-++++++-++-+++-+--+-+---+-+-+++--++--/| | |
||||  |||||  |||| |  ||| |||||||  |  | |||| ||  |/-++-+++++--+++--++--+--++-++---+--+++---+-+--+--+---+-+++-++++++\\|| ||| |  | |   | | |||  ||   | | |
||||  |||||  |||| |  ||| |||||||  |  | |||| ||  || || |||||  |||  ||  \\--++-++---+--+++---+-+--+--+---+-+++-+++++++++-+++-+--+-+---+-+-+++--++---/ | |
||||  |||||  |||| |  ||| |||||||  |  | |||| ||  || || |||||  |||  |\\-----++-++---+--+++---+-+--+--+---+-+++-+/||||||| ||| |  | |   | | |||  ||     | |
||||  |||||/-++++-+--+++-+++++++--+--+-++++-++--++-++-+++++--+++--+------++-++--\\|  |||   | |  |  |   | ||| | ||||||| ||| |  | |   | | \\++--++-----+-/
||||  |||||| |||| |  ||| |||||||  |  | |||| ||  || || |||||  |||  |      || ||  ||  |||   | |  |  |   | ||| | ||||||| ||| |  | |   | |  ||  ||     |
||||  |||||| |||| | /+++-+++++++--+--+-++++-++--++-++-+++++--+++--+------++-++--++--+++---+-+--+--+--\\| ||| | ||||||| ||| |  | |   | |  ||  ||     |
||||  |||||| |||| | |||| |||||||  |  | |||| ||  || || |||||  |||  |      || ||  ||  |||   | |  |  |  || ||| | ||||||| ||| |  | |   | |  ||  ||     |
||||  |||||| |||| | |||| |||||||  |  | |||| ||  || || |||||  |||  \\------++-++--++--+++---+-+--+--+--++-+++-+-+++++++-+++-+--+-+---+-/  ||  ||     |
||||  |||||| |||| | |||| ||\\++++--+--+-++++-++--++-++-+++++--++/         || ||  ||  |||   |/+--+--+--++-+++\\| ||||||| ||| |  |/+---+---\\||  ||     |
||||  |||||| |||| | |||| || ||||  |  | |||| \\+--++-++-+++++--++----------/| ||  ||  |||   |||  |  |  || ||||| ||||||| ||| |  |||   |   |||  ||     |
||||  ||||\\+-++++-+-+/|| |^ ||||  |  | ||||/-+--++-++-+++++--++-----------+-++--++--+++---+++--+--+--++-+++++-+++++++-+++-+--+++---+---+++--++---\\ |
||||  |||| | ||||/+-+-++-++-++++-\\|  | ||||| |  || || ||||\\--++-----------+-++--++--+++---+++--+--+--++-+++++-+++++++-+++-+--/||   |   |||  ||   | |
||||  |||| | ||\\+++-+-++-++-++++-++--+-+++++-+--++-++-++++---++-----------+-++--++--+++---+++--+--+--++-+++++-+++/||| ||| |   ||   |   |||  ||   | |
||||  ||\\+-+-++-+++-+-++-++-++++-++--+-+++++-+--++-++-++++---++-----------+-++--++--+++---+++--+--+--++-++++/ ||| ||| ||| |   ||   |   |||  ||   | |
||||  || | | || ||| | || || |||| ||  | ||||| |  || || ||||   ||           | ||  ||  ||\\---+++--+--+--++-++++--+++-+++-+++-+---++---+---+++--/|   | |
||||  || | | || ||| | || |\\-++++-++--+-+++++-+--++-++-++++---++-----------+-++--++--++----+++--+--+--++-++++--+++-+++-+++-+---+/   |   |||   |   | |
||||  || | | || ||| | || |  |||| ||  | ||||| |  || || ||||   ||/----------+-++--++--++----+++--+--+--++-++++--+++-+++-+++-+---+----+---+++---+---+-+-\\
||||  || | | || ||| | || |  |||| ||  | |\\+++-+--++-++-++++---+++----------+-++--++--++----+++--+--+--++-++++--/|| ||| ||| |   |    |   |||   |   | | |
||||  || | | || ||| \\-++-+--++++-++--+-+-+++-+--++-++-++++---+++----------+-++--++--++----+++--+--+--/| ||||   || ||| ||| |   |    |   |||   |   | | |
||||  \\+-+-+-++-+++---++-+--++++-++--+-+-+++-+--++-++-++++---+++----------+-++--++--/|    |||  |  |   | ||||   || ||| ||| |   |    |   |||   |   | | |
||||   | | | || |||   || |  |\\++-++--+-+-+++-+--++-++-++++---+++----------+-++--++---+----+++--+--+---+-++++---++-++/ ||| |   |    |   |||   |   | | |
||||   | | | || |\\+---++-+--+-++-/|  \\-+-+++-+--++-++-++++---+++----------+-++--++---+----+++--+--+---+-++++---++-++--+/| |   |    |   |||   |   | | |
\\+++---+-+-+-++-+-+---++-+--+-++--+----+-+++-+--++-/| |||\\---+++----------+-/|  ||   |    \\++--+--+---+-++++---+/ ||  | | |   |    |   |||   |   | | |
 |||/--+-+-+-++-+-+---++-+->+-++--+-\\  | ||| |  ||  | |||    \\++----------+--+--++---+-----++--+--+---+-++++---+--++--+-+-+---+----/   |||   |   | | |
 ||||  | | | || | |   || |  | ||  | |  | ||| |  ||  | |^|     ||          |  |  ||   |     \\+--+--+---+-+++/   |  ||  | | |   |        |||   |   | | |
 ||||  | | | |\\-+-+---++-+--+-++--+-+--+-+++-+--++--+-+++-----++----------+--+--++---+------+--+--+---+-+++----+--++--+-+-/   |        |||   |   | | |
 ||||  | | | |  | |   || |  | ||  | |  | ||| |  ||  | |||     ||         /+--+--++---+------+--+--+---+-+++----+--++--+-+-----+-\\      |||   |   | | |
 ||||  | | | |  | \\---++-+--+-++--+-+--+-+++-+--++--+-+++-----++---------++--/  ||   |      |  |  |   | |||    |  ||  | |     | |    /-+++---+\\  | | |
 ||\\+--+-+-+-+--+-----++-+--+-++--+-+--+-+++-+--++--+-+++-----++---------++-----++---/      |  |  |   | |||    |  ||  | |     | |    | |||   ||  | | |
 || |  | | | |  |     || |/-+-++--+\\|  | ||| |  ||/-+-+++--\\  ||         ||     ||          |  |  |   | |||    |  ||  | |     | |    | |||   ||  | | |
 || |  | | | |  |     || || | ||  |||  | |||/+--+++-+\\|||  |  ||         ||     ||          |  |  |   | |||    |  ||  | |     | |    | |||   ||  | | |
 || |  | | | \\--+-----++-++-+-++--+++--+-+++++--+++-+++++--+--++---------++-----+/          |  |  |   | |||    |  ||  | |     \\-+----+-/||   ||  | | |
 || |  | | |    |     || || | ||  |||  | |||||  ||| |||||  |  ||         ||     |           |  |  |   | |||    |  ||  | |       |    |  ||   ||  | | |
 || |  | | |    |     \\+-++-+-++--+++--+-+/|||  ||| |||||  |  ||         ||     |           |  |  |   | |||    |  ||  | |       |    |  ||   ||  | | |
 || |  | | |    |      | || | ||  |||  | | |||  ||| \\++++--+--++---------++-----+-----------+--/  |   | |||    |  ||  | |       |    |  ||   ||  | | |
 || |  \\-+-+----+------+-++-+-++--+++--+-+-+++--+++--++++--+--++---------++-----+-----------+-----+---/ |||    |  ||  | |       |    |  ||   ||  | | |
 || |    | |    |      | || | ||  |||  | \\-+++--+++--+/|| /+--++---------++-----+-----------+-----+----\\|||    |  ||  | |       |    |  ||   ||  | | |
 || |    | |    |      | || | ||  ||v  |   |||  |||  | || ||  ||         ||     |           |     |    ||||    |  ||  | |       |    |  ||   ||  | | |
 || |    | \\----+------+-++-+-++--+++--+---+++--+++--+-++-++--++---------++-----/           |     |    ||||    |  ||  | |       |    |  ||   ||  | | |
 || |    |      ^      | || | ||  |||  |   |||  |||  | |\\-++--++---------++-----------------+-----+----++++----+--++--+-+-------+----+--++---++--+-/ |
 || |    |      \\------+-++-+-++--/||  |   |||  \\++--+-+--++--++---------++-----------------+-----+----++++----+--++--+-/       |    |  ||   ||  |   |
 || |    |             | || | ||   ||  |   |||   ||  | |  ||  ||         ||                 |     |    ||||    |  ||  |         |    |  ||   ||  |   |
 || |    |             | \\+-+-++---++--+---+++---++--+-+--++--++---------++-----------------/     |    ||||    |  ||  |         |    |  ||   ||  |   |
 || |    |             |  | \\-++---++--+---+++---++--+-+--++--++---------++-----------------------+----++++----+--++--/         |    |  ||   ||  |   |
 \\+-+----+-------------+--+---/|   ||  |   |||   ||  | |  ||  ||         ||                       \\----++++----+--++------------+----+--/|   ||  |   |
  | |    |             |  |    \\---++--+---+++---++--+-+--++--++---------++----------------------------++++----/  ||            |    |   |   ||  |   |
  \\-+----+-------------+--+--------++--+---+++---++--+-+--++--++---------++----------------------------+/|\\-------+/            |    |   |   ||  |   |
    |    |             |  |        ||  |   |||   ||  | |  \\+--++---------++--------------------<-------/ |        |             |    |   |   ||  |   |
    |    |             |  |        ||  |   |||   \\+--+-+---+--++---------++------------------------------+--------/             |    |   |   ||  |   |
    |    |             |  |        ||  |   |||    \\--+-+---/  ||         ||                              |                      |    |   |   ||  |   |
    |    |             \\--+--------++--+---+++-------+-+------++---------++------------------------------/                      |    |   |   ||  |   |
    \\----+----------------+--------+/  |   |||       | |      ||         \\+-----------------------------------------------------/    \\---+---+/  |   |
         |                |        |   |   \\++-------+-+------++----------+--------------------------------------------------------------+---+---/   |
         |                |        |   |    ||       | |      |\\----------+--------------------------------------------------------------+---+-------/
         |                \\--------/   |    |\\-------+-+------/           |                                                              |   |
         |                             |    |        | \\------------------+--------------------------------------------------------------/   |
         \\-----------------------------/    \\--------/                    \\------------------------------------------------------------------/""".split("\n")

initial_state2 = """/>-<\\
|   |
| /<+-\\
| | | v
\\>+</ |
  |   ^
  \\<->/""".split("\n")

state = initial_state
DIRECTIONS = "<^>v"

from enum import Enum
class TurnDir(Enum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2

class Car(object):
    def __init__(self, y, x, dir, underneath, choice=TurnDir.LEFT):
        self.y = y
        self.x = x
        self.dir = dir
        self.choice = choice
        self.underneath = underneath

    def __repr__(self):
        return f"({self.y},{self.x} {self.dir})"

cars = []
for (y, row) in enumerate(state):
    for (x, c) in enumerate(row):
        if c in "<>":
            cars.append(Car(y, x, underneath="-", dir=c))
        elif c in "^v":
            cars.append(Car(y, x, underneath="|", dir=c))

def move_car(car):
    dx = 0
    dy = 0
    if car.dir == "<":
        dx = -1
    elif car.dir == ">":
        dx = 1
    elif car.dir == "^":
        dy = -1
    elif car.dir == "v":
        dy = 1

    next_dir = car.dir
    next_spot = state[car.y + dy][car.x + dx]
    next_choice = car.choice
    if next_spot in DIRECTIONS:
        other_car = None
        for (i, c) in enumerate(cars):
            if c and car and c.x == car.x + dx and c.y == car.y + dy:
                other_car = i
                state[c.y] = state[c.y][:c.x] + c.underneath + state[c.y][c.x+1:]
                break
        assert other_car != None
        state[car.y] = state[car.y][:car.x] + car.underneath + state[car.y][car.x+1:]
        return (cars.index(car), other_car)
    else:
        if next_spot == "+":
            if car.choice == TurnDir.LEFT:
                next_dir = DIRECTIONS[abs((DIRECTIONS.index(car.dir) - 1) % len(DIRECTIONS))]
            elif car.choice == TurnDir.RIGHT:
                next_dir = DIRECTIONS[(DIRECTIONS.index(car.dir) + 1) % len(DIRECTIONS)]
            next_choice = TurnDir((car.choice.value + 1) % 3)
        elif next_spot == "\\":
            if car.dir == ">":
                next_dir = "v"
            elif car.dir == "^":
                next_dir = "<"
            elif car.dir == "v":
                next_dir = ">"
            elif car.dir == "<":
                next_dir = "^"
        elif next_spot == "/":
            if car.dir == ">":
                next_dir = "^"
            elif car.dir == "^":
                next_dir = ">"
            elif car.dir == "v":
                next_dir = "<"
            elif car.dir == "<":
                next_dir = "v"

        state[car.y] = state[car.y][:car.x] + car.underneath + state[car.y][car.x+1:]
        state[car.y+dy] = state[car.y+dy][:car.x+dx] + next_dir + state[car.y+dy][car.x+dx+1:]
        return Car(car.y + dy, car.x + dx, dir=next_dir, underneath=next_spot, choice=next_choice)


def sort_cars(cars):
    return sorted(cars, key=lambda car: (car.y, car.x))

tick = 0
while len(cars) > 1:
    cars = sort_cars(cars)
    # print(tick)
    # print(cars)
    # for line in state:
    #     print(line)
    for (i, car) in enumerate(cars):
        if car:
            new_car = move_car(car)
            if type(new_car) == Car:
                cars[i] = new_car
            else:
                cars[new_car[0]] = None
                cars[new_car[1]] = None
    cars = [car for car in cars if car]
    tick += 1

assert len(cars) == 1
print(f"{cars[0].x},{cars[0].y}")
