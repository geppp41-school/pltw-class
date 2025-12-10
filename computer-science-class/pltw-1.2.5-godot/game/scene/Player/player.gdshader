shader_type canvas_item;
//uniform float fill_percent = 0.5;
uniform float fill_percent = 1.0;
uniform vec4 full : source_color = vec4(1.0, 1.0, 1.0, 1.0);
uniform vec4 empty : source_color = vec4(0.5, 0.5, 0.5, 0.1);

void vertex() {
	//COLOR = vec4(UV.x, UV.y, 1.0, 1.0);
	// Called for every vertex the material is visible on.
}

void fragment() {
	if(COLOR != vec4(0.0, 0.0, 0.0, 0.0)){
		if(COLOR.q >= 0.2){
			if(UV.x	< 0.5 && UV.x > 0.5-1.0*(fill_percent*0.37)){
				COLOR = full;
			} else if(UV.x > 0.5 && UV.x < 0.5+1.0*(fill_percent*0.37)){
				COLOR = full;
			} else {
				COLOR = empty;
			}
			
		} 
	}
	 //Called for every pixel the material is visible on.
}

//void light() {
//	// Called for every pixel for every light affecting the CanvasItem.
//	// Uncomment to replace the default light processing function with this one.
//}
