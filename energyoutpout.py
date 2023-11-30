def expression(inputs) : 
if type(inputs) != list:
print('Argument must be a list')
return
if len(inputs) != 4:
print('Incorrect number of inputs')
return
temperature=inputs[0]
exhaustt_vacuum=inputs[1]
ambient_pressure=inputs[2]
relative_humidity=inputs[3]
scaled_temperature = (temperature-19.6512)/7.45247
scaled_exhaustt_vacuum = 2*(exhaustt_vacuum-25.36)/(81.56-25.36)-1
scaled_ambient_pressure = (ambient_pressure-1013.26)/5.93878
scaled_relative_humidity = (relative_humidity-73.309)/14.6003
		y_1_1 = tanh (-0.155062+ (scaled_temperature*0.203034)+ (scaled_exhaustt_vacuum*0.731056)+ (scaled_ambient_pressure*-0.191671)+ (scaled_relative_humidity*0.0158643))
		y_1_2 = tanh (-0.29098+ (scaled_temperature*-0.023069)+ (scaled_exhaustt_vacuum*-0.263476)+ (scaled_ambient_pressure*-0.231774)+ (scaled_relative_humidity*0.333626))
		y_1_3 = tanh (0.570558+ (scaled_temperature*0.573079)+ (scaled_exhaustt_vacuum*-0.0279703)+ (scaled_ambient_pressure*0.111165)+ (scaled_relative_humidity*0.00867248))
		scaled_energy_output =  (0.15981+ (y_1_1*-0.383639)+ (y_1_2*-0.126028)+ (y_1_3*-0.745885))
energy_output = (0.5*(scaled_energy_output+1.0)*(495.76-420.26)+420.26)
		return energy_output 