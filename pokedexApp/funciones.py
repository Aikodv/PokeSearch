
primera = ['bulbasaur', 'charmander', 'squirtle', 'caterpie', 'weedle', 'pidgey', 'rattata', 'spearow', 'ekans', 'sandshrew', 'nidoran-f', 'nidoran-m', 'vulpix', 'zubat', 'oddish', 'paras', 'venonat', 'diglett', 'meowth', 'psyduck', 'mankey', 'growlithe', 'poliwag', 'abra', 'machop', 'bellsprout', 'tentacool', 'geodude', 'venusaur', 'charmeleon', 'charizard', 'wartortle', 'blastoise', 'metapod', 'butterfree', 'kakuna', 'beedrill', 'pidgeotto', 'pidgeot', 'raticate', 'fearow', 'arbok', 'pikachu', 'raichu', 'sandslash', 'nidorina', 'nidoqueen', 'nidorino', 'nidoking', 'clefairy', 'clefable', 'ninetales', 'jigglypuff', 'wigglytuff', 'golbat', 'gloom', 'vileplume', 'parasect', 'venomoth', 'dugtrio', 'persian', 'golduck', 'primeape', 'arcanine', 'poliwhirl', 'poliwrath', 'kadabra', 'alakazam', 'machoke', 'machamp', 'weepinbell', 'victreebel', 'tentacruel', 'graveler', 'ponyta', 'slowpoke', 'magnemite', 'farfetchd', 'doduo', 'seel', 'grimer', 'shellder', 'gastly', 'onix', 'drowzee', 'krabby', 'voltorb', 'exeggcute', 'cubone', 'lickitung', 'koffing', 'rhyhorn', 'tangela', 'kangaskhan', 'horsea', 'goldeen', 'staryu', 'scyther', 'pinsir', 'tauros', 'magikarp', 'lapras', 'ditto', 'eevee', 'porygon', 'omanyte', 'kabuto', 'aerodactyl', 'articuno', 'zapdos', 'moltres', 'dratini', 'mewtwo', 'rapidash', 'slowbro', 'magneton', 'dodrio', 'dewgong', 'muk', 'cloyster', 'haunter', 'gengar', 'hypno', 'kingler', 'electrode', 'exeggutor', 'marowak', 'hitmonlee', 'hitmonchan', 'weezing', 'rhydon', 'chansey', 'seadra', 'seaking', 'starmie', 'mr-mime', 'jynx', 'electabuzz', 'magmar', 'gyarados', 'vaporeon', 'jolteon', 'flareon', 'omastar', 'kabutops', 'snorlax', 'dragonair', 'dragonite', 'mew', 'ivysaur', 'golem']
a = ['charmander', 'charmeleon', 'charizard', 'vulpix', 'ninetales', 'growlithe', 'arcanine', 'ponyta', 'rapidash', 'magmar', 'flareon', 'moltres', 'cyndaquil', 'quilava', 'typhlosion', 'slugma', 'magcargo', 'houndour', 'houndoom', 'magby', 'entei', 'ho-oh', 'torchic', 'combusken', 'blaziken', 'numel', 'camerupt', 'torkoal', 'chimchar', 'monferno', 'infernape', 'magmortar', 'heatran', 'victini', 'tepig', 'pignite', 'emboar', 'pansear', 'simisear', 'darumaka', 'darmanitan-standard', 'litwick', 'lampent', 'chandelure', 'heatmor', 'larvesta', 'volcarona', 'reshiram', 'fennekin', 'braixen', 'delphox', 'fletchinder', 'talonflame', 'litleo', 'pyroar', 'volcanion', 'litten', 'torracat', 'incineroar', 'oricorio-baile', 'salandit', 'salazzle', 'turtonator', 'blacephalon', 'scorbunny', 'raboot', 'cinderace', 'carkol', 'coalossal', 'sizzlipede', 'centiskorch', 'rotom-heat', 'castform-sunny', 'darmanitan-zen', 'charizard-mega-x', 'charizard-mega-y', 'houndoom-mega', 'blaziken-mega', 'groudon-primal', 'camerupt-mega', 'marowak-alola', 'salazzle-totem', 'marowak-totem', 'darmanitan-galar-zen', 'charizard-gmax', 'cinderace-gmax', 'coalossal-gmax', 'centiskorch-gmax', 'growlithe-hisui', 'arcanine-hisui', 'typhlosion-hisui']
# intersect primera y a
primera_a = [x for x in primera if x in a]
print(primera_a)