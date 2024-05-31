import json
def generate_objects():

    x_start = 48
    z_start = 48
    x2_start = 0
    z2_start = 48
    
    x_decrement = x_start-x2_start
    z_decrement = z_start-z2_start
    
    x_end = -48
    z_end = -48
    
    id_start = 4
    rotation_x = 0
    rotation_y = 0
    rotation_z = 0
    rotation_w = 1
    object_guid = "79fef3a74aa3dd10b6fc758d376064bd"
    subobject_type_id = 5
    position_type_id = 8
    rotation_type_id = 9
    rotation_value_id = 10

    objects = []
    current_id = id_start
    current_x = x_start
    

    while current_x > x_end:
        current_z = z_start
        while current_z > z_end:
            print(current_x, current_z)
            obj = f"""                        {{
                            "$id": {current_id},
                            "$type": {subobject_type_id},
                            "m_Object": $fstrref:"UnityGUID:{object_guid}",
                            "m_Position": {{
                                "$type": {position_type_id},
                                "x": {current_x},
                                "y": 35,
                                "z": {current_z}
                            }},
                            "m_Rotation": {{
                                "$type": {rotation_type_id},
                                "value": {{
                                    "$type": {rotation_value_id},
                                    "x": {rotation_x},
                                    "y": {rotation_y},
                                    "z": {rotation_z},
                                    "w": {rotation_w}
                                }}
                            }},
                            "m_ParentMesh": 12,
                            "m_GroupIndex": 0,
                            "m_Probability": 100
                        }}"""
            objects.append(obj)
            current_id += 1
            current_z = round(current_z - z_decrement, 3)
        current_x = round(current_x - x_decrement, 3)
    
    print(f"{current_id-1000} objects created")
    return objects

objects = generate_objects()
text_output = ",\n".join(objects)
with open('output.txt', 'w') as f:
    f.write(text_output)
