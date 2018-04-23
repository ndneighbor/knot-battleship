# knot-battleship

Knot-Battleship is a game that breaks the rules of normal battleship. There are new conditions that are added to the game such as...

1. You can make teams, you can assign colors to the teams, the more teams, the more ships that are assigned, therefore it is possible to hit two ships that the same time provided that they are in the same grid location.

2. There is the ability to have multiple teams of players controlling one set of battleships. All teammates have their own board and every team member has their own shot given to them. Each team has a team lead that will allow them to pick where the ships belong.

3. Each player gets one shot, but it is not synced. Each team will go and pick up to three shots. Each member of the team can pick a shot- if the team size is >3 then you assign a new shot to them

4. If a team is eliminated, the team that had the most shots on that team will get the medal of killing the team.

5. If a team resigns, the above principle applies to the team that leaves.

6. If all teams resigns- we calculate it on points, one point for hits- the tie breaker is the amount of misses the team aquired.

Added Notes

- There needs to be feedback about what's going 

- There needs to be help menu to understand

- Teams should be able to chat between their team members, all users regardless of team, or message to the other team. 

## Technical Implementation

The following project will be split up into two parts, the client will just mostly send websocket commands over to the server and interpret the visual state- the server will store game state and will handle chat while sending render updates to the interface.

## Client Methods

## Server Methods