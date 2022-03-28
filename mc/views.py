
from django.shortcuts import render
import joblib
# Create your views here.



def index(request):
    return render(request, 'index.html')

def inputs(request):
    return render(request, 'inputs.html')

def result(request):
    classification_model = joblib.load('mushroom_classification_model.sav')
    inputs = []

    cap_shape = str(request.POST['cap_shape'])
    if cap_shape== "b":
        cap_shape_b = 1
        cap_shape_c =0
        cap_shape_x=0
        cap_shape_f =0
        cap_shape_k=0
        cap_shape_s=0
        inputs.extend([cap_shape_b,cap_shape_c,cap_shape_x,cap_shape_f,cap_shape_k,cap_shape_s])
    elif cap_shape== "c":
        cap_shape_b = 0
        cap_shape_c =1
        cap_shape_x=0
        cap_shape_f =0
        cap_shape_k=0
        cap_shape_s=0
        inputs.extend([cap_shape_b,cap_shape_c,cap_shape_x,cap_shape_f,cap_shape_k,cap_shape_s])
    elif cap_shape== "x":
        cap_shape_b = 0
        cap_shape_c =0
        cap_shape_x=1
        cap_shape_f =0
        cap_shape_k=0
        cap_shape_s=0
        inputs.extend([cap_shape_b,cap_shape_c,cap_shape_x,cap_shape_f,cap_shape_k,cap_shape_s])
    elif cap_shape== "f":
        cap_shape_b = 0
        cap_shape_c =0
        cap_shape_x=0
        cap_shape_f =1
        cap_shape_k=0
        cap_shape_s=0
        inputs.extend([cap_shape_b,cap_shape_c,cap_shape_x,cap_shape_f,cap_shape_k,cap_shape_s])
    elif cap_shape== "k":
        cap_shape_b = 0
        cap_shape_c =0
        cap_shape_x=0
        cap_shape_f =0
        cap_shape_k=1
        cap_shape_s=0
        inputs.extend([cap_shape_b,cap_shape_c,cap_shape_x,cap_shape_f,cap_shape_k,cap_shape_s])
    elif cap_shape== "s":
        cap_shape_b = 0
        cap_shape_c =0
        cap_shape_x=0
        cap_shape_f =0
        cap_shape_k=0
        cap_shape_s=1
        inputs.extend([cap_shape_b,cap_shape_c,cap_shape_x,cap_shape_f,cap_shape_k,cap_shape_s])
    else:
        print("Error in Cap Shape")



    cap_surface = str(request.POST['cap_surface'])
    if cap_surface == "f":
        cap_surface_f = 1
        cap_surface_g = 0
        cap_surface_y = 0
        cap_surface_s = 0
        inputs.extend([cap_surface_f, cap_surface_g, cap_surface_y, cap_surface_s])
    elif cap_surface == "g":
        cap_surface_f = 0
        cap_surface_g = 1
        cap_surface_y = 0
        cap_surface_s = 0
        inputs.extend([cap_surface_f, cap_surface_g, cap_surface_y, cap_surface_s])
    elif cap_surface == "y":
        cap_surface_f = 0
        cap_surface_g = 0
        cap_surface_y = 1
        cap_surface_s = 0
        inputs.extend([cap_surface_f, cap_surface_g, cap_surface_y, cap_surface_s])
    elif cap_surface == "s":
        cap_surface_f = 0
        cap_surface_g = 0
        cap_surface_y = 0
        cap_surface_s = 1
        inputs.extend([cap_surface_f, cap_surface_g, cap_surface_y, cap_surface_s])
    else :
        print("error in Cap Surface")


    cap_color = str(request.POST['cap_color'])
    if cap_color == "n":
        cap_color_n =1
        cap_color_b = 0
        cap_color_c =0
        cap_color_g=0
        cap_color_r=0
        cap_color_p=0
        cap_color_u=0
        cap_color_e=0
        cap_color_w=0
        cap_color_y=0
        inputs.extend([cap_color_n,cap_color_b, cap_color_c, cap_color_g, cap_color_r, cap_color_p, cap_color_u, cap_color_e, cap_color_w, cap_color_y])

    elif cap_color == "b":
        cap_color_n = 0
        cap_color_b = 1
        cap_color_c =0
        cap_color_g=0
        cap_color_r=0
        cap_color_p=0
        cap_color_u=0
        cap_color_e=0
        cap_color_w=0
        cap_color_y=0
        inputs.extend([cap_color_n,cap_color_b, cap_color_c, cap_color_g, cap_color_r, cap_color_p, cap_color_u, cap_color_e, cap_color_w, cap_color_y])
    elif cap_color == "c":
        cap_color_n = 0
        cap_color_b = 0
        cap_color_c =1
        cap_color_g=0
        cap_color_r=0
        cap_color_p=0
        cap_color_u=0
        cap_color_e=0
        cap_color_w=0
        cap_color_y=0
        inputs.extend([cap_color_n,cap_color_b, cap_color_c, cap_color_g, cap_color_r, cap_color_p, cap_color_u, cap_color_e, cap_color_w, cap_color_y])
    elif cap_color == "g":
        cap_color_n = 0
        cap_color_b = 0
        cap_color_c =0
        cap_color_g=1
        cap_color_r=0
        cap_color_p=0
        cap_color_u=0
        cap_color_e=0
        cap_color_w=0
        cap_color_y=0
        inputs.extend([cap_color_n,cap_color_b, cap_color_c, cap_color_g, cap_color_r, cap_color_p, cap_color_u, cap_color_e, cap_color_w, cap_color_y])
    elif cap_color == "r":
        cap_color_n = 0
        cap_color_b = 0
        cap_color_c =0
        cap_color_g=0
        cap_color_r=1
        cap_color_p=0
        cap_color_u=0
        cap_color_e=0
        cap_color_w=0
        cap_color_y=0
        inputs.extend([cap_color_n,cap_color_b, cap_color_c, cap_color_g, cap_color_r, cap_color_p, cap_color_u, cap_color_e, cap_color_w, cap_color_y])
    elif cap_color == "p":
        cap_color_n = 0
        cap_color_b = 0
        cap_color_c =0
        cap_color_g=0
        cap_color_r=0
        cap_color_p=1
        cap_color_u=0
        cap_color_e=0
        cap_color_w=0
        cap_color_y=0
        inputs.extend([cap_color_n,cap_color_b, cap_color_c, cap_color_g, cap_color_r, cap_color_p, cap_color_u, cap_color_e, cap_color_w, cap_color_y])
    elif cap_color == "u":
        cap_color_n = 0
        cap_color_b = 0
        cap_color_c =0
        cap_color_g=0
        cap_color_r=0
        cap_color_p=0
        cap_color_u=1
        cap_color_e=0
        cap_color_w=0
        cap_color_y=0
        inputs.extend([cap_color_n,cap_color_b, cap_color_c, cap_color_g, cap_color_r, cap_color_p, cap_color_u, cap_color_e, cap_color_w, cap_color_y])
    elif cap_color == "e":
        cap_color_n = 0
        cap_color_b = 0
        cap_color_c =0
        cap_color_g=0
        cap_color_r=0
        cap_color_p=0
        cap_color_u=0
        cap_color_e=1
        cap_color_w=0
        cap_color_y=0
        inputs.extend([cap_color_n,cap_color_b, cap_color_c, cap_color_g, cap_color_r, cap_color_p, cap_color_u, cap_color_e, cap_color_w, cap_color_y])
    elif cap_color == "w":
        cap_color_n = 0
        cap_color_b = 0
        cap_color_c =0
        cap_color_g=0
        cap_color_r=0
        cap_color_p=0
        cap_color_u=0
        cap_color_e=0
        cap_color_w=1
        cap_color_y=0
        inputs.extend([cap_color_n,cap_color_b, cap_color_c, cap_color_g, cap_color_r, cap_color_p, cap_color_u, cap_color_e, cap_color_w, cap_color_y])
    elif cap_color == "y":
        cap_color_n = 0
        cap_color_b = 0
        cap_color_c =0
        cap_color_g=0
        cap_color_r=0
        cap_color_p=0
        cap_color_u=0
        cap_color_e=0
        cap_color_w=0
        cap_color_y=1
        inputs.extend([cap_color_n,cap_color_b, cap_color_c, cap_color_g, cap_color_r, cap_color_p, cap_color_u, cap_color_e, cap_color_w, cap_color_y])
    else:
        print("Error in Cap Color")


    bruises = str(request.POST['bruises'])
    if bruises == "t":
        bruises_t = 1
        bruises_f = 0
        inputs.extend([bruises_t, bruises_f])
    elif bruises == "t":
        bruises_t = 1
        bruises_f = 0
        inputs.extend([bruises_t, bruises_f])
    else:
        print("Error in Bruises")

    






    odor = str(request.POST['odor'])
    if odor == "a":
        odor_a =1
        odor_l=0
        odor_c =0
        odor_y =0
        odor_f=0
        odor_m=0
        odor_n=0
        odor_p=0
        odor_s=0
        inputs.extend([odor_a,odor_l, odor_c, odor_y, odor_f, odor_m, odor_n, odor_p, odor_s])
    elif odor == "l":
        odor_a =0
        odor_l=1
        odor_c =0
        odor_y =0
        odor_f=0
        odor_m=0
        odor_n=0
        odor_p=0
        odor_s=0
        inputs.extend([odor_a,odor_l, odor_c, odor_y, odor_f, odor_m, odor_n, odor_p, odor_s])
    elif odor == "c":
        odor_a =0
        odor_l=0
        odor_c =1
        odor_y =0
        odor_f=0
        odor_m=0
        odor_n=0
        odor_p=0
        odor_s=0
        inputs.extend([odor_a,odor_l, odor_c, odor_y, odor_f, odor_m, odor_n, odor_p, odor_s])
    elif odor == "y":
        odor_a =0
        odor_l=0
        odor_c =0
        odor_y =1
        odor_f=0
        odor_m=0
        odor_n=0
        odor_p=0
        odor_s=0
        inputs.extend([odor_a,odor_l, odor_c, odor_y, odor_f, odor_m, odor_n, odor_p, odor_s])
    elif odor == "f":
        odor_a =0
        odor_l=0
        odor_c =0
        odor_y =0
        odor_f=1
        odor_m=0
        odor_n=0
        odor_p=0
        odor_s=0
        inputs.extend([odor_a,odor_l, odor_c, odor_y, odor_f, odor_m, odor_n, odor_p, odor_s])
    elif odor == "m":
        odor_a =0
        odor_l=0
        odor_c =0
        odor_y =0
        odor_f=0
        odor_m=1
        odor_n=0
        odor_p=0
        odor_s=0
        inputs.extend([odor_a,odor_l, odor_c, odor_y, odor_f, odor_m, odor_n, odor_p, odor_s])
    elif odor == "n":
        odor_a =0
        odor_l=0
        odor_c =0
        odor_y =0
        odor_f=0
        odor_m=0
        odor_n=1
        odor_p=0
        odor_s=0
        inputs.extend([odor_a,odor_l, odor_c, odor_y, odor_f, odor_m, odor_n, odor_p, odor_s])
    elif odor == "p":
        odor_a =0
        odor_l=0
        odor_c =0
        odor_y =0
        odor_f=0
        odor_m=0
        odor_n=0
        odor_p=1
        odor_s=0
        inputs.extend([odor_a,odor_l, odor_c, odor_y, odor_f, odor_m, odor_n, odor_p, odor_s])
    elif odor == "s":
        odor_a =0
        odor_l=0
        odor_c =0
        odor_y =0
        odor_f=0
        odor_m=0
        odor_n=0
        odor_p=0
        odor_s=1
        inputs.extend([odor_a,odor_l, odor_c, odor_y, odor_f, odor_m, odor_n, odor_p, odor_s])
    else:
        print("Error in Odor")

    
    gill_attachment = str(request.POST['gill_attachment'])
    if gill_attachment== "a":
        gill_attachment_a=1
       
        gill_attachment_f=0
        
        inputs.extend([gill_attachment_a, gill_attachment_f])
    
    elif gill_attachment=="f":
        gill_attachment_a=0
       
        gill_attachment_f=1
        
        inputs.extend([gill_attachment_a,  gill_attachment_f])
    
    else:
        print("Error in Gill Atttachement")


    gill_spacing = str(request.POST['gill_spacing'])
    if gill_spacing=="c":
        gill_spacing_c=1
        gill_spacing_w=0
        
        inputs.extend([gill_spacing_c, gill_spacing_w, ])
    elif gill_spacing=="w":
        gill_spacing_c=0
        gill_spacing_w=1
        
        inputs.extend([gill_spacing_c, gill_spacing_w, ])
    elif gill_spacing=="d":
        gill_spacing_c=0
        gill_spacing_w=0
        
        inputs.extend([gill_spacing_c, gill_spacing_w, ])
    else:
        print("Error in Gill Spacing")

    gill_size = str(request.POST['gill_size'])
    if gill_size=="b":
        gill_size_b=1
        gill_size_n=0
        inputs.extend([gill_size_b, gill_size_n])
    elif gill_size=="n":
        gill_size_b=0
        gill_size_n=1
        inputs.extend([gill_size_b, gill_size_n])
    else:
        print("Error in Gill Size")


    gill_color = str(request.POST['gill_color'])
    if gill_color=="k":
        gill_color_k=1
        gill_color_n=0
        gill_color_b=0
        gill_color_h=0
        gill_color_g=0
        gill_color_r=0
        gill_color_o=0
        gill_color_p=0
        gill_color_u=0
        gill_color_e=0
        gill_color_w=0
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="n":
        gill_color_k=0
        gill_color_n=1
        gill_color_b=0
        gill_color_h=0
        gill_color_g=0
        gill_color_r=0
        gill_color_o=0
        gill_color_p=0
        gill_color_u=0
        gill_color_e=0
        gill_color_w=0
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="b":
        gill_color_k=0
        gill_color_n=0
        gill_color_b=1
        gill_color_h=0
        gill_color_g=0
        gill_color_r=0
        gill_color_o=0
        gill_color_p=0
        gill_color_u=0
        gill_color_e=0
        gill_color_w=0
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="h":
        gill_color_k=0
        gill_color_n=0
        gill_color_b=0
        gill_color_h=1
        gill_color_g=0
        gill_color_r=0
        gill_color_o=0
        gill_color_p=0
        gill_color_u=0
        gill_color_e=0
        gill_color_w=0
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="g":
        gill_color_k=0
        gill_color_n=0
        gill_color_b=0
        gill_color_h=0
        gill_color_g=1
        gill_color_r=0
        gill_color_o=0
        gill_color_p=0
        gill_color_u=0
        gill_color_e=0
        gill_color_w=0
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="r":
        gill_color_k=0
        gill_color_n=0
        gill_color_b=0
        gill_color_h=0
        gill_color_g=0
        gill_color_r=1
        gill_color_o=0
        gill_color_p=0
        gill_color_u=0
        gill_color_e=0
        gill_color_w=0
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="o":
        gill_color_k=0
        gill_color_n=0
        gill_color_b=0
        gill_color_h=0
        gill_color_g=0
        gill_color_r=0
        gill_color_o=1
        gill_color_p=0
        gill_color_u=0
        gill_color_e=0
        gill_color_w=0
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="p":
        gill_color_k=0
        gill_color_n=0
        gill_color_b=0
        gill_color_h=0
        gill_color_g=0
        gill_color_r=0
        gill_color_o=0
        gill_color_p=1
        gill_color_u=0
        gill_color_e=0
        gill_color_w=0
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="u":
        gill_color_k=0
        gill_color_n=0
        gill_color_b=0
        gill_color_h=0
        gill_color_g=0
        gill_color_r=0
        gill_color_o=0
        gill_color_p=0
        gill_color_u=1
        gill_color_e=0
        gill_color_w=0
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="e":
        gill_color_k=0
        gill_color_n=0
        gill_color_b=0
        gill_color_h=0
        gill_color_g=0
        gill_color_r=0
        gill_color_o=0
        gill_color_p=0
        gill_color_u=0
        gill_color_e=1
        gill_color_w=0
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="w":
        gill_color_k=0
        gill_color_n=0
        gill_color_b=0
        gill_color_h=0
        gill_color_g=0
        gill_color_r=0
        gill_color_o=0
        gill_color_p=0
        gill_color_u=0
        gill_color_e=0
        gill_color_w=1
        gill_color_y=0
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    elif gill_color=="y":
        gill_color_k=0
        gill_color_n=0
        gill_color_b=0
        gill_color_h=0
        gill_color_g=0
        gill_color_r=0
        gill_color_o=0
        gill_color_p=0
        gill_color_u=0
        gill_color_e=0
        gill_color_w=0
        gill_color_y=1
        inputs.extend([gill_color_k, gill_color_n, gill_color_b, gill_color_h, gill_color_g, gill_color_r, gill_color_o,gill_color_p,gill_color_u,gill_color_e,gill_color_w,gill_color_y,])
    else:
        print("Error in Gill Colour")



    stalk_shape = str(request.POST['stalk_shape'])
    if stalk_shape=="e":
        stalk_shape_e=1
        stalk_shape_t=0
        inputs.extend([stalk_shape_e, stalk_shape_t])
    elif stalk_shape=="t":
        stalk_shape_e=0
        stalk_shape_t=1
        inputs.extend([stalk_shape_e, stalk_shape_t])
    else:
        print("Error in Stalk Shape")
    


   
    stalk_root = str(request.POST['stalk_root'])
    if stalk_root=="b":
        stalk_root_b=1
        stalk_root_c=0
        stalk_root_e=0
        stalk_root_r=0
        stalk_root_z=0
        inputs.extend([stalk_root_b,stalk_root_c,stalk_root_e,stalk_root_r,stalk_root_z])
    elif stalk_root=="c":
        stalk_root_b=0
        stalk_root_c=1
        
        stalk_root_e=0
        stalk_root_r=0
        stalk_root_z=0
        inputs.extend([stalk_root_b,stalk_root_c,stalk_root_e,stalk_root_r,stalk_root_z])
    elif stalk_root=="u":
        stalk_root_b=0
        stalk_root_c=0
        
        stalk_root_e=0
        stalk_root_r=0
        stalk_root_z=0
        inputs.extend([stalk_root_b,stalk_root_c,stalk_root_e,stalk_root_r,stalk_root_z])
    elif stalk_root=="e":
        stalk_root_b=0
        stalk_root_c=0
        
        stalk_root_e=1
        stalk_root_r=0
        stalk_root_z=0
        inputs.extend([stalk_root_b,stalk_root_c,stalk_root_e,stalk_root_r,stalk_root_z])
    elif stalk_root=="z":
        stalk_root_b=0
        stalk_root_c=0
        
        stalk_root_e=0
        stalk_root_r=0
        stalk_root_z=1
        inputs.extend([stalk_root_b,stalk_root_c,stalk_root_e,stalk_root_r,stalk_root_z])
    else:
        print("Error in Stalk Root")

    
    stalk_surface_above_ring= str(request.POST['stalk_surface_above_ring'])
    if stalk_surface_above_ring=="f":
        stalk_surface_above_ring_f=1
        stalk_surface_above_ring_y=0
        stalk_surface_above_ring_k=0
        stalk_surface_above_ring_s=0
        inputs.extend([stalk_surface_above_ring_f,stalk_surface_above_ring_y,stalk_surface_above_ring_k,stalk_surface_above_ring_s,])
    elif stalk_surface_above_ring=="y":
        stalk_surface_above_ring_f=0
        stalk_surface_above_ring_y=1
        stalk_surface_above_ring_k=0
        stalk_surface_above_ring_s=0
        inputs.extend([stalk_surface_above_ring_f,stalk_surface_above_ring_y,stalk_surface_above_ring_k,stalk_surface_above_ring_s,])
    elif stalk_surface_above_ring=="k":
        stalk_surface_above_ring_f=0
        stalk_surface_above_ring_y=0
        stalk_surface_above_ring_k=1
        stalk_surface_above_ring_s=0
        inputs.extend([stalk_surface_above_ring_f,stalk_surface_above_ring_y,stalk_surface_above_ring_k,stalk_surface_above_ring_s,])
    elif stalk_surface_above_ring=="s":
        stalk_surface_above_ring_f=0
        stalk_surface_above_ring_y=0
        stalk_surface_above_ring_k=0
        stalk_surface_above_ring_s=1
        inputs.extend([stalk_surface_above_ring_f,stalk_surface_above_ring_y,stalk_surface_above_ring_k,stalk_surface_above_ring_s,])
    else:
        print("Error in Stalk Surface Above Ring")










    stalk_surface_below_ring = str(request.POST['stalk_surface_below_ring'])
    if stalk_surface_below_ring=="f":
        stalk_surface_below_ring_f=1
        stalk_surface_below_ring_y=0
        stalk_surface_below_ring_k=0
        stalk_surface_below_ring_s=0
        inputs.extend([stalk_surface_below_ring_f,stalk_surface_below_ring_y,stalk_surface_below_ring_k,stalk_surface_below_ring_s,])
    elif stalk_surface_below_ring=="y":
        stalk_surface_below_ring_f=0
        stalk_surface_below_ring_y=1
        stalk_surface_below_ring_k=0
        stalk_surface_below_ring_s=0
        inputs.extend([stalk_surface_below_ring_f,stalk_surface_below_ring_y,stalk_surface_below_ring_k,stalk_surface_below_ring_s,])
    elif stalk_surface_below_ring=="k":
        stalk_surface_below_ring_f=0
        stalk_surface_below_ring_y=0
        stalk_surface_below_ring_k=1
        stalk_surface_below_ring_s=0
        inputs.extend([stalk_surface_below_ring_f,stalk_surface_below_ring_y,stalk_surface_below_ring_k,stalk_surface_below_ring_s,])
    elif stalk_surface_below_ring=="s":
        stalk_surface_below_ring_f=0
        stalk_surface_below_ring_y=0
        stalk_surface_below_ring_k=0
        stalk_surface_below_ring_s=1
        inputs.extend([stalk_surface_below_ring_f,stalk_surface_below_ring_y,stalk_surface_below_ring_k,stalk_surface_below_ring_s,])
    else:
        print("Error in Stalk Surface Below Ring")


    stalk_color_above_ring = str(request.POST['stalk_color_above_ring'])
    if stalk_color_above_ring=="n":
        stalk_color_above_ring_n=1
        stalk_color_above_ring_b=0
        stalk_color_above_ring_c=0
        stalk_color_above_ring_g=0
        stalk_color_above_ring_o=0
        stalk_color_above_ring_p=0
        stalk_color_above_ring_e=0
        stalk_color_above_ring_w=0
        stalk_color_above_ring_y=0
        inputs.extend([stalk_color_above_ring_n,stalk_color_above_ring_b,stalk_color_above_ring_c,stalk_color_above_ring_g,stalk_color_above_ring_o,stalk_color_above_ring_p,stalk_color_above_ring_e,stalk_color_above_ring_w,stalk_color_above_ring_y,])
    elif stalk_color_above_ring=="b":
        stalk_color_above_ring_n=0
        stalk_color_above_ring_b=1
        stalk_color_above_ring_c=0
        stalk_color_above_ring_g=0
        stalk_color_above_ring_o=0
        stalk_color_above_ring_p=0
        stalk_color_above_ring_e=0
        stalk_color_above_ring_w=0
        stalk_color_above_ring_y=0
        inputs.extend([stalk_color_above_ring_n,stalk_color_above_ring_b,stalk_color_above_ring_c,stalk_color_above_ring_g,stalk_color_above_ring_o,stalk_color_above_ring_p,stalk_color_above_ring_e,stalk_color_above_ring_w,stalk_color_above_ring_y,])
    elif stalk_color_above_ring=="c":
        stalk_color_above_ring_n=0
        stalk_color_above_ring_b=0
        stalk_color_above_ring_c=1
        stalk_color_above_ring_g=0
        stalk_color_above_ring_o=0
        stalk_color_above_ring_p=0
        stalk_color_above_ring_e=0
        stalk_color_above_ring_w=0
        stalk_color_above_ring_y=0
        inputs.extend([stalk_color_above_ring_n,stalk_color_above_ring_b,stalk_color_above_ring_c,stalk_color_above_ring_g,stalk_color_above_ring_o,stalk_color_above_ring_p,stalk_color_above_ring_e,stalk_color_above_ring_w,stalk_color_above_ring_y,])
    elif stalk_color_above_ring=="g":
        stalk_color_above_ring_n=0
        stalk_color_above_ring_b=0
        stalk_color_above_ring_c=0
        stalk_color_above_ring_g=1
        stalk_color_above_ring_o=0
        stalk_color_above_ring_p=0
        stalk_color_above_ring_e=0
        stalk_color_above_ring_w=0
        stalk_color_above_ring_y=0
        inputs.extend([stalk_color_above_ring_n,stalk_color_above_ring_b,stalk_color_above_ring_c,stalk_color_above_ring_g,stalk_color_above_ring_o,stalk_color_above_ring_p,stalk_color_above_ring_e,stalk_color_above_ring_w,stalk_color_above_ring_y,])
    elif stalk_color_above_ring=="o":
        stalk_color_above_ring_n=0
        stalk_color_above_ring_b=0
        stalk_color_above_ring_c=0
        stalk_color_above_ring_g=0
        stalk_color_above_ring_o=1
        stalk_color_above_ring_p=0
        stalk_color_above_ring_e=0
        stalk_color_above_ring_w=0
        stalk_color_above_ring_y=0
        inputs.extend([stalk_color_above_ring_n,stalk_color_above_ring_b,stalk_color_above_ring_c,stalk_color_above_ring_g,stalk_color_above_ring_o,stalk_color_above_ring_p,stalk_color_above_ring_e,stalk_color_above_ring_w,stalk_color_above_ring_y,])
    elif stalk_color_above_ring=="p":
        stalk_color_above_ring_n=0
        stalk_color_above_ring_b=0
        stalk_color_above_ring_c=0
        stalk_color_above_ring_g=0
        stalk_color_above_ring_o=0
        stalk_color_above_ring_p=1
        stalk_color_above_ring_e=0
        stalk_color_above_ring_w=0
        stalk_color_above_ring_y=0
        inputs.extend([stalk_color_above_ring_n,stalk_color_above_ring_b,stalk_color_above_ring_c,stalk_color_above_ring_g,stalk_color_above_ring_o,stalk_color_above_ring_p,stalk_color_above_ring_e,stalk_color_above_ring_w,stalk_color_above_ring_y,])
    elif stalk_color_above_ring=="e":
        stalk_color_above_ring_n=0
        stalk_color_above_ring_b=0
        stalk_color_above_ring_c=0
        stalk_color_above_ring_g=0
        stalk_color_above_ring_o=0
        stalk_color_above_ring_p=0
        stalk_color_above_ring_e=1
        stalk_color_above_ring_w=0
        stalk_color_above_ring_y=0
        inputs.extend([stalk_color_above_ring_n,stalk_color_above_ring_b,stalk_color_above_ring_c,stalk_color_above_ring_g,stalk_color_above_ring_o,stalk_color_above_ring_p,stalk_color_above_ring_e,stalk_color_above_ring_w,stalk_color_above_ring_y,])
    elif stalk_color_above_ring=="w":
        stalk_color_above_ring_n=0
        stalk_color_above_ring_b=0
        stalk_color_above_ring_c=0
        stalk_color_above_ring_g=0
        stalk_color_above_ring_o=0
        stalk_color_above_ring_p=0
        stalk_color_above_ring_e=0
        stalk_color_above_ring_w=1
        stalk_color_above_ring_y=0
        inputs.extend([stalk_color_above_ring_n,stalk_color_above_ring_b,stalk_color_above_ring_c,stalk_color_above_ring_g,stalk_color_above_ring_o,stalk_color_above_ring_p,stalk_color_above_ring_e,stalk_color_above_ring_w,stalk_color_above_ring_y,])
    elif stalk_color_above_ring=="y":
        stalk_color_above_ring_n=0
        stalk_color_above_ring_b=0
        stalk_color_above_ring_c=0
        stalk_color_above_ring_g=0
        stalk_color_above_ring_o=0
        stalk_color_above_ring_p=0
        stalk_color_above_ring_e=0
        stalk_color_above_ring_w=0
        stalk_color_above_ring_y=1
        inputs.extend([stalk_color_above_ring_n,stalk_color_above_ring_b,stalk_color_above_ring_c,stalk_color_above_ring_g,stalk_color_above_ring_o,stalk_color_above_ring_p,stalk_color_above_ring_e,stalk_color_above_ring_w,stalk_color_above_ring_y,])
    else:
        print("Error in Stalk Colour above ring")


    
    stalk_color_below_ring = str(request.POST['stalk_color_below_ring'])
    if stalk_color_below_ring=="n":
        stalk_color_below_ring_n=1
        stalk_color_below_ring_b=0
        stalk_color_below_ring_c=0
        stalk_color_below_ring_g=0
        stalk_color_below_ring_o=0
        stalk_color_below_ring_p=0
        stalk_color_below_ring_e=0
        stalk_color_below_ring_w=0
        stalk_color_below_ring_y=0
        inputs.extend([stalk_color_below_ring_n,stalk_color_below_ring_b,stalk_color_below_ring_c,stalk_color_below_ring_g,stalk_color_below_ring_o,stalk_color_below_ring_p,stalk_color_below_ring_e,stalk_color_below_ring_w,stalk_color_below_ring_y,])
    elif stalk_color_below_ring=="b":
        stalk_color_below_ring_n=0
        stalk_color_below_ring_b=1
        stalk_color_below_ring_c=0
        stalk_color_below_ring_g=0
        stalk_color_below_ring_o=0
        stalk_color_below_ring_p=0
        stalk_color_below_ring_e=0
        stalk_color_below_ring_w=0
        stalk_color_below_ring_y=0
        inputs.extend([stalk_color_below_ring_n,stalk_color_below_ring_b,stalk_color_below_ring_c,stalk_color_below_ring_g,stalk_color_below_ring_o,stalk_color_below_ring_p,stalk_color_below_ring_e,stalk_color_below_ring_w,stalk_color_below_ring_y,])
    elif stalk_color_below_ring=="c":
        stalk_color_below_ring_n=0
        stalk_color_below_ring_b=0
        stalk_color_below_ring_c=1
        stalk_color_below_ring_g=0
        stalk_color_below_ring_o=0
        stalk_color_below_ring_p=0
        stalk_color_below_ring_e=0
        stalk_color_below_ring_w=0
        stalk_color_below_ring_y=0
        inputs.extend([stalk_color_below_ring_n,stalk_color_below_ring_b,stalk_color_below_ring_c,stalk_color_below_ring_g,stalk_color_below_ring_o,stalk_color_below_ring_p,stalk_color_below_ring_e,stalk_color_below_ring_w,stalk_color_below_ring_y,])
    elif stalk_color_below_ring=="g":
        stalk_color_below_ring_n=0
        stalk_color_below_ring_b=0
        stalk_color_below_ring_c=0
        stalk_color_below_ring_g=1
        stalk_color_below_ring_o=0
        stalk_color_below_ring_p=0
        stalk_color_below_ring_e=0
        stalk_color_below_ring_w=0
        stalk_color_below_ring_y=0
        inputs.extend([stalk_color_below_ring_n,stalk_color_below_ring_b,stalk_color_below_ring_c,stalk_color_below_ring_g,stalk_color_below_ring_o,stalk_color_below_ring_p,stalk_color_below_ring_e,stalk_color_below_ring_w,stalk_color_below_ring_y,])
    elif stalk_color_below_ring=="o":
        stalk_color_below_ring_n=0
        stalk_color_below_ring_b=0
        stalk_color_below_ring_c=0
        stalk_color_below_ring_g=0
        stalk_color_below_ring_o=1
        stalk_color_below_ring_p=0
        stalk_color_below_ring_e=0
        stalk_color_below_ring_w=0
        stalk_color_below_ring_y=0
        inputs.extend([stalk_color_below_ring_n,stalk_color_below_ring_b,stalk_color_below_ring_c,stalk_color_below_ring_g,stalk_color_below_ring_o,stalk_color_below_ring_p,stalk_color_below_ring_e,stalk_color_below_ring_w,stalk_color_below_ring_y,])
    elif stalk_color_below_ring=="p":
        stalk_color_below_ring_n=0
        stalk_color_below_ring_b=0
        stalk_color_below_ring_c=0
        stalk_color_below_ring_g=0
        stalk_color_below_ring_o=0
        stalk_color_below_ring_p=1
        stalk_color_below_ring_e=0
        stalk_color_below_ring_w=0
        stalk_color_below_ring_y=0
        inputs.extend([stalk_color_below_ring_n,stalk_color_below_ring_b,stalk_color_below_ring_c,stalk_color_below_ring_g,stalk_color_below_ring_o,stalk_color_below_ring_p,stalk_color_below_ring_e,stalk_color_below_ring_w,stalk_color_below_ring_y,])
    elif stalk_color_below_ring=="e":
        stalk_color_below_ring_n=0
        stalk_color_below_ring_b=0
        stalk_color_below_ring_c=0
        stalk_color_below_ring_g=0
        stalk_color_below_ring_o=0
        stalk_color_below_ring_p=0
        stalk_color_below_ring_e=1
        stalk_color_below_ring_w=0
        stalk_color_below_ring_y=0
        inputs.extend([stalk_color_below_ring_n,stalk_color_below_ring_b,stalk_color_below_ring_c,stalk_color_below_ring_g,stalk_color_below_ring_o,stalk_color_below_ring_p,stalk_color_below_ring_e,stalk_color_below_ring_w,stalk_color_below_ring_y,])
    elif stalk_color_below_ring=="w":
        stalk_color_below_ring_n=0
        stalk_color_below_ring_b=0
        stalk_color_below_ring_c=0
        stalk_color_below_ring_g=0
        stalk_color_below_ring_o=0
        stalk_color_below_ring_p=0
        stalk_color_below_ring_e=0
        stalk_color_below_ring_w=1
        stalk_color_below_ring_y=0
        inputs.extend([stalk_color_below_ring_n,stalk_color_below_ring_b,stalk_color_below_ring_c,stalk_color_below_ring_g,stalk_color_below_ring_o,stalk_color_below_ring_p,stalk_color_below_ring_e,stalk_color_below_ring_w,stalk_color_below_ring_y,])
    elif stalk_color_below_ring=="y":
        stalk_color_below_ring_n=0
        stalk_color_below_ring_b=0
        stalk_color_below_ring_c=0
        stalk_color_below_ring_g=0
        stalk_color_below_ring_o=0
        stalk_color_below_ring_p=0
        stalk_color_below_ring_e=0
        stalk_color_below_ring_w=0
        stalk_color_below_ring_y=1
        inputs.extend([stalk_color_below_ring_n,stalk_color_below_ring_b,stalk_color_below_ring_c,stalk_color_below_ring_g,stalk_color_below_ring_o,stalk_color_below_ring_p,stalk_color_below_ring_e,stalk_color_below_ring_w,stalk_color_below_ring_y,])
    else:
        print("Error in Stalk Colour below ring")



    veil_type = str(request.POST['veil_type'])
    if veil_type=="p":
        veil_type_p=1
        inputs.extend([veil_type_p])
    
    else:
        print("Error in veil_type")

    veil_color = str(request.POST['veil_color'])
    if veil_color=="n":
        veil_color_n=1
        veil_color_o=0
        veil_color_w=0
        veil_color_y=0
        inputs.extend([veil_color_n,veil_color_o,veil_color_w,veil_color_y])
    elif veil_color=="o":
        veil_color_n=0
        veil_color_o=1
        veil_color_w=0
        veil_color_y=0
        inputs.extend([veil_color_n,veil_color_o,veil_color_w,veil_color_y])
    elif veil_color=="w":
        veil_color_n=0
        veil_color_o=0
        veil_color_w=1
        veil_color_y=0
        inputs.extend([veil_color_n,veil_color_o,veil_color_w,veil_color_y])
    elif veil_color=="y":
        veil_color_n=0
        veil_color_o=0
        veil_color_w=0
        veil_color_y=1
        inputs.extend([veil_color_n,veil_color_o,veil_color_w,veil_color_y])
    else:
        print("Error in Veil Color")

    ring_number= str(request.POST['ring_number'])
    if ring_number=="n":
        ring_number_n=1
        ring_number_o=0
        ring_number_t=0
        inputs.extend([ring_number_n,ring_number_o,ring_number_t,])
    elif ring_number=="o":
        ring_number_n=0
        ring_number_o=1
        ring_number_t=0
        inputs.extend([ring_number_n,ring_number_o,ring_number_t,])
    elif ring_number=="t":
        ring_number_n=0
        ring_number_o=0
        ring_number_t=1
        inputs.extend([ring_number_n,ring_number_o,ring_number_t,])
    else:
        print("Error in Ring number")



    
    ring_type = str(request.POST['ring_type'])
    
    if ring_type=="e":
        
        ring_type_e=1
        ring_type_f=0
        ring_type_l=0
        ring_type_n=0
        ring_type_p=0
        
        inputs.extend([ring_type_e,ring_type_f,ring_type_l,ring_type_n,ring_type_p])
    elif ring_type=="f":
        
        ring_type_e=0
        ring_type_f=1
        ring_type_l=0
        ring_type_n=0
        ring_type_p=0
        
        inputs.extend([ring_type_e,ring_type_f,ring_type_l,ring_type_n,ring_type_p])
    elif ring_type=="l":
        
        ring_type_e=0
        ring_type_f=0
        ring_type_l=1
        ring_type_n=0
        ring_type_p=0
        
        inputs.extend([ring_type_e,ring_type_f,ring_type_l,ring_type_n,ring_type_p])
    elif ring_type=="n":
        
        ring_type_e=0
        ring_type_f=0
        ring_type_l=0
        ring_type_n=1
        ring_type_p=0
        
        inputs.extend([ring_type_e,ring_type_f,ring_type_l,ring_type_n,ring_type_p])
    elif ring_type=="p":
       
        ring_type_e=0
        ring_type_f=0
        ring_type_l=0
        ring_type_n=0
        ring_type_p=1
        
        inputs.extend([ring_type_e,ring_type_f,ring_type_l,ring_type_n,ring_type_p])
    
    else:
        print("Error in Ring Type")
    

    spore_print_color = str(request.POST['spore_print_color'])
    if spore_print_color=="k":
        spore_print_color_k=1
        spore_print_color_n=0
        spore_print_color_b=0
        spore_print_color_h=0
        spore_print_color_r=0
        spore_print_color_o=0
        spore_print_color_u=0
        spore_print_color_w=0
        spore_print_color_y=0
        inputs.extend([spore_print_color_k,spore_print_color_n,spore_print_color_b,spore_print_color_h,spore_print_color_r,spore_print_color_o,spore_print_color_u,spore_print_color_w,spore_print_color_y,])
    elif spore_print_color=="n":
        spore_print_color_k=0
        spore_print_color_n=1
        spore_print_color_b=0
        spore_print_color_h=0
        spore_print_color_r=0
        spore_print_color_o=0
        spore_print_color_u=0
        spore_print_color_w=0
        spore_print_color_y=0
        inputs.extend([spore_print_color_k,spore_print_color_n,spore_print_color_b,spore_print_color_h,spore_print_color_r,spore_print_color_o,spore_print_color_u,spore_print_color_w,spore_print_color_y,])
    elif spore_print_color=="b":
        spore_print_color_k=0
        spore_print_color_n=0
        spore_print_color_b=1
        spore_print_color_h=0
        spore_print_color_r=0
        spore_print_color_o=0
        spore_print_color_u=0
        spore_print_color_w=0
        spore_print_color_y=0
        inputs.extend([spore_print_color_k,spore_print_color_n,spore_print_color_b,spore_print_color_h,spore_print_color_r,spore_print_color_o,spore_print_color_u,spore_print_color_w,spore_print_color_y,])
    elif spore_print_color=="h":
        spore_print_color_k=0
        spore_print_color_n=0
        spore_print_color_b=0
        spore_print_color_h=1
        spore_print_color_r=0
        spore_print_color_o=0
        spore_print_color_u=0
        spore_print_color_w=0
        spore_print_color_y=0
        inputs.extend([spore_print_color_k,spore_print_color_n,spore_print_color_b,spore_print_color_h,spore_print_color_r,spore_print_color_o,spore_print_color_u,spore_print_color_w,spore_print_color_y,])
    elif spore_print_color=="r":
        spore_print_color_k=0
        spore_print_color_n=0
        spore_print_color_b=0
        spore_print_color_h=0
        spore_print_color_r=1
        spore_print_color_o=0
        spore_print_color_u=0
        spore_print_color_w=0
        spore_print_color_y=0
        inputs.extend([spore_print_color_k,spore_print_color_n,spore_print_color_b,spore_print_color_h,spore_print_color_r,spore_print_color_o,spore_print_color_u,spore_print_color_w,spore_print_color_y,])
    elif spore_print_color=="o":
        spore_print_color_k=0
        spore_print_color_n=0
        spore_print_color_b=0
        spore_print_color_h=0
        spore_print_color_r=0
        spore_print_color_o=1
        spore_print_color_u=0
        spore_print_color_w=0
        spore_print_color_y=0
        inputs.extend([spore_print_color_k,spore_print_color_n,spore_print_color_b,spore_print_color_h,spore_print_color_r,spore_print_color_o,spore_print_color_u,spore_print_color_w,spore_print_color_y,])    
    elif spore_print_color=="u":
        spore_print_color_k=0
        spore_print_color_n=0
        spore_print_color_b=0
        spore_print_color_h=0
        spore_print_color_r=0
        spore_print_color_o=0
        spore_print_color_u=1
        spore_print_color_w=0
        spore_print_color_y=0
        inputs.extend([spore_print_color_k,spore_print_color_n,spore_print_color_b,spore_print_color_h,spore_print_color_r,spore_print_color_o,spore_print_color_u,spore_print_color_w,spore_print_color_y,])
    elif spore_print_color=="w":
        spore_print_color_k=0
        spore_print_color_n=0
        spore_print_color_b=0
        spore_print_color_h=0
        spore_print_color_r=0
        spore_print_color_o=0
        spore_print_color_u=0
        spore_print_color_w=1
        spore_print_color_y=0
        inputs.extend([spore_print_color_k,spore_print_color_n,spore_print_color_b,spore_print_color_h,spore_print_color_r,spore_print_color_o,spore_print_color_u,spore_print_color_w,spore_print_color_y,])
    elif spore_print_color=="y":
        spore_print_color_k=0
        spore_print_color_n=0
        spore_print_color_b=0
        spore_print_color_h=0
        spore_print_color_r=0
        spore_print_color_o=0
        spore_print_color_u=0
        spore_print_color_w=0
        spore_print_color_y=1
        inputs.extend([spore_print_color_k,spore_print_color_n,spore_print_color_b,spore_print_color_h,spore_print_color_r,spore_print_color_o,spore_print_color_u,spore_print_color_w,spore_print_color_y,])
    else:
        print("Error in Spore Print Color")
    
    
    population = str(request.POST['population'])
    if population=="a":
        population_a=1
        population_c=0
        population_n=0
        population_s=0
        population_v=0
        population_y=0
        inputs.extend([population_a,population_c,population_n,population_s,population_v,population_y,])
    elif population=="c":
        population_a=0
        population_c=1
        population_n=0
        population_s=0
        population_v=0
        population_y=0
        inputs.extend([population_a,population_c,population_n,population_s,population_v,population_y,])
    elif population=="n":
        population_a=0
        population_c=0
        population_n=1
        population_s=0
        population_v=0
        population_y=0
        inputs.extend([population_a,population_c,population_n,population_s,population_v,population_y,])
    elif population=="s":
        population_a=0
        population_c=0
        population_n=0
        population_s=1
        population_v=0
        population_y=0
        inputs.extend([population_a,population_c,population_n,population_s,population_v,population_y,])
    elif population=="v":
        population_a=0
        population_c=0
        population_n=0
        population_s=0
        population_v=1
        population_y=0
        inputs.extend([population_a,population_c,population_n,population_s,population_v,population_y,])
    elif population=="y":
        population_a=0
        population_c=0
        population_n=0
        population_s=0
        population_v=0
        population_y=1
        inputs.extend([population_a,population_c,population_n,population_s,population_v,population_y,])
    else:
        print("Error in Population")



    
    habitat = str(request.POST['habitat'])
    if habitat=="g":
        habitat_g=1
        habitat_l=0
        habitat_m=0
        habitat_p=0
        habitat_u=0
        habitat_w=0
        habitat_d=0
        inputs.extend([habitat_g,habitat_l,habitat_m,habitat_p,habitat_u,habitat_w,habitat_d,])
    elif habitat=="l":
        habitat_g=0
        habitat_l=1
        habitat_m=0
        habitat_p=0
        habitat_u=0
        habitat_w=0
        habitat_d=0
        inputs.extend([habitat_g,habitat_l,habitat_m,habitat_p,habitat_u,habitat_w,habitat_d,])
    elif habitat=="m":
        habitat_g=0
        habitat_l=0
        habitat_m=1
        habitat_p=0
        habitat_u=0
        habitat_w=0
        habitat_d=0
        inputs.extend([habitat_g,habitat_l,habitat_m,habitat_p,habitat_u,habitat_w,habitat_d,])
    elif habitat=="p":
        habitat_g=0
        habitat_l=0
        habitat_m=0
        habitat_p=1
        habitat_u=0
        habitat_w=0
        habitat_d=0
        inputs.extend([habitat_g,habitat_l,habitat_m,habitat_p,habitat_u,habitat_w,habitat_d,])
    elif habitat=="u":
        habitat_g=0
        habitat_l=1
        habitat_m=0
        habitat_p=0
        habitat_u=1
        habitat_w=0
        habitat_d=0
        inputs.extend([habitat_g,habitat_l,habitat_m,habitat_p,habitat_u,habitat_w,habitat_d,])
    elif habitat=="w":
        habitat_g=0
        habitat_l=1
        habitat_m=0
        habitat_p=0
        habitat_u=0
        habitat_w=1
        habitat_d=0
        inputs.extend([habitat_g,habitat_l,habitat_m,habitat_p,habitat_u,habitat_w,habitat_d,])
    elif habitat=="d":
        habitat_g=0
        habitat_l=1
        habitat_m=0
        habitat_p=0
        habitat_u=0
        habitat_w=0
        habitat_d=1
        inputs.extend([habitat_g,habitat_l,habitat_m,habitat_p,habitat_u,habitat_w,habitat_d,])


    

    # if len(inputs) != 117:
    #     while len(inputs) < 117:
    #         inputs.append(0)
            
        
    classified_answer = classification_model.predict([inputs])
    pred = classified_answer.flatten()
    if pred==1:
        ans = "EDIBLE"
    elif pred==0:
        ans ="POISONOUS"
    else:
        print("Error in Result")
    return render(request, 'result.html', {'ans':ans})
