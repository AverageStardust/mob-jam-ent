# MobJam 2025 Submission - Team wheeeee
<h3> Member: Lyra, Peini, Wren and Clover
 
Link to our Github repository: https://github.com/AverageStardust/mob-jam-ent

# Mob Description
<b> Name:</b> Ent <br>
<b> Biome:</b> Dark forest
  
## Behavior
### Spawn
After spawning, the ent will sit there quietly disgusing as a dark oak tree. They will not follow or attack any player during this phase. However, any player that gets too close to the ent will see a warning message.
### Emerge
Once the ent got damaged, they will emerge from the ground and start attacking nearby players. Every nearby player will get a warning message that the ent is activated.
### Break blocks
Due to the dense natural of the dark forest, a giant mob like the ent struggles to move around freely. That's why the ent will break all the leave blocks in front of them while walking. Once the targeted player runs too far away from the ent, they will cast a sonic boom to destroy every leave, log and mushroom blocks in front of them.
### Melee attack
The ent will kick player's ass if they gets too close.
### Ranged attack
The ent will perform a ranged attack on players entering the range once the cooldown has ended. The player will be pushed away from the ent and receive slightly more damage than a melee attack. The attack range is indicated with green particles and every player in the range will get a warning message one second before the attack.
### Place berry bush
Once the ent gets attacked by the player, they will attempt to place berry bushes to trap the player in a circle. This is an effective way to slow down the players and prevent them from escaping. The berry bush circle will disappear after three seconds.

# File Structure
We created a custom ent model that contains sick animations for each of the behaviours descirbed above. However, every file must be placed in the correct location for the model to be displayed properly.
## yml files
There are three crucial yml files [ent_phase_idle.yml](ent_phase_idle.yml), [ent_phase_1.yml](ent_phase_1.yml) and [ent_phase_death.yml](ent_phase_death.yml) that should go under the folder `server\plugins\EliteMobs\custombosses`
## bbmodel files
There are two crucial blockbench model files [ent_boss_model_0.bbmodel](ent_boss_model_0.bbmodel) and [ent_boss_model_1.bbmodel](ent_boss_model_1.bbmodel) that should go under the folder `server\plugins\ModelEngine\blueprints`
## Resource pack
The ent resource pack should be enabled for every player.
