import numpy as np
import numpy
import matplotlib.pyplot as plt

def signalDraw(n,x_n,t):
    fig=plt.figure()
    plt.title(t)
    ax=fig.add_subplot(111)
    
    ax.stem(n,x_n)
def UnitImpulse(lb,ub):
    assert(lb<=ub),"lower bound can,t grateer than upper bound"
    n=np.arange(lb,ub+1,1)
    #print(n)
    x_n=[]
    for i in n:
        if i<0:
         x_n.append(0)
        elif i==0:
           x_n.append(1)
        else:
            x_n.append(0)
    
   
    x_n=np.array(x_n)
    
    return (n,x_n)
def UnitRamp(lb,ub):
    assert(lb<=ub),"lower bound can,t grateer than upper bound"
    n=np.arange(lb,ub+1,1)
    #print(n)
    x_n=[]
    for i in n:
        if i>=0:
         x_n.append(i)
        
        else:
            x_n.append(0)
    
   
    x_n=np.array(x_n)
    
    return (n,x_n)
def UnitStep(lb,ub):
    assert(lb<=ub),"lower bound can,t grateer than upper bound"
    n=np.arange(lb,ub+1,1)
    #print(n)
    x_n=[]
    for i in n:
        if i>=0:
         x_n.append(1)
        
        else:
            x_n.append(0)
    
   
    x_n=np.array(x_n)
    
    return (n,x_n)

def mirroring(original):
    
    n=original[0]
    x_m=original[1]
#    signalDraw(n,x_m,"mir1")

    x_m=x_m[::-1]
    

            
    
#    signalDraw(n,x_m,"mir")
    return(n,x_m)
            
   
def Downsampling(original,dA ):
    n=original[0]
    x_n=original[1]

    dict={}
    c=0
    y_n=[]
    for i in range(len(x_n)):
        y_n.append(0)
    for i in n:
        dict[i]=c;
        c=c+1
    mn=n[0]
    mx=n[len(x_n)-1]
    
    for i in range(mn,mx):
        if((i*dA)<mn or (i*dA)>mx):
            y_n[dict[i]]=0
        else:
            y_n[dict[i]]=x_n[dict[i*dA]]    
    
    return (n,y_n)
        
def amplitude(original,A):
    
    n=original[0]
    x_n=original[1]
    
    y=A*x_n
    y=np.array(y)
    return(n,y)
    
def Add(a,b):
    n=a[0]
    x1=a[1]
    n1=b[0]
    x2=b[1]
    


    mn=min(n[0],n1[0])
    mx=max(n[len(n)-1],n1[len(n1)-1])
    
    y_n=[]
    n3=[]
    
    for i in range(mn,mx+1):
        n3.append(i)
        y_n.append(0)
        
    j=0
    
    for i in range(abs(n[0]-n3[0]),abs(n[0]-n3[0])+(len(n))):
        y_n[i]+=x1[j]
        j+=1
    
    j=0
    
    for i in range(abs(n1[0]-n3[0]),abs(n1[0]-n3[0])+(len(n1))):
        y_n[i]+=x2[j]
        j+=1

    return (n3,y_n)  
    
    


def Subtract(a,b):
    n=a[0]
    x1=a[1]
    n1=b[0]
    x2=b[1]
    mn=min(n[0],n1[0])
    mx=max(n[len(n)-1],n1[len(n1)-1])
    
    
    y_n=[]
    n3=[]
    
    for i in range(mn,mx+1):
        n3.append(i)
        y_n.append(0)
    j=0
    
    for i in range(abs(n[0]-n3[0]),abs(n[0]-n3[0])+(len(n))):
        y_n[i]+=x1[j]
        j+=1
    
    j=0
    for i in range(abs(n1[0]-n3[0]),abs(n1[0]-n3[0])+(len(n1))):
        y_n[i]-=x2[j]
        j+=1

    return (n3,y_n) 
 
def Multiply(a,b):

    n=a[0]
    x1=a[1]
    n1=b[0]
    x2=b[1]    

    mn=min(n[0],n1[0])
    mx=max(n[len(n)-1],n1[len(n1)-1])
    
    y_n=[]
    n3=[]
    
    for i in range(mn,mx+1):
        n3.append(i)
        y_n.append(0)
    j=0
    for i in range(abs(n[0]-n3[0]),abs(n[0]-n3[0])+(len(n))):
        y_n[i]+=x1[j]
        j+=1
    
    j=0
    for i in range(abs(n1[0]-n3[0]),abs(n1[0]-n3[0])+(len(n1))):
        y_n[i]*=x2[j]
        j+=1

    return (n3,y_n)     
    
    
def timeshifting(originalSiganal,shftingAmount): 
     n,x_n=originalSiganal
     y_n=np.zeros(n.shape[0])
     
     if shftingAmount>0:
         if shftingAmount>n.shape[0]:
             shftingAmount=n.shape[0]
         dataTocopy = x_n [:n.shape[0]-shftingAmount]
         y_n[shftingAmount : ]=dataTocopy
     elif shftingAmount<0:
         if abs(shftingAmount)>n.shape[0]:
             shftingAmount=n.shape[0]*-1
         dataTocopy=x_n[-shftingAmount:]
         y_n[:n.shape[0]+shftingAmount]=dataTocopy
     else:
         y_n=x_n
     return(n,y_n)
     
if __name__ == "__main__":
    
    
    text_file=open("input.text","r")
    all_input=[]
   
    for line in text_file:
        
        splitted_line = line.split(' ')
        for values in splitted_line:
            
            val = int(values)
            
            all_input.append(val)
    
    all_input=np.array(all_input)
    print(all_input)
    track=0
    test_case=all_input[track]
    
    #print("test case",test_case)
    
    while(test_case>0):
        track=track+1
        comp_part=all_input[track]
#        print("two comp part",comp_part,track)
        test_case=test_case-1
        comp=-1
        comp_p=[]
        
        
        
        while(comp_part>0):
            track=track+1
            lb=all_input[track]
#            print("lower",lb,track)
            track=track+1
            ub=all_input[track]
            #print("upper",ub,track)
            track=track+1
            signal=-1
            signal_p=[]
            
            signal_part=all_input[track]
            #print("signalpart",signal_part,track)
            
            comp_part=comp_part-1

            while(signal_part>0):
                
                track=track+1
                am=0
                if (all_input[track]==1):
                    print("not amplitude",all_input[track])
                    am=1
                else:
                    
                    
                    #print("amplitude",all_input[track],track)
                    am=all_input[track]
                signal_part=signal_part-1
                #impulse cheak
                track=track+1
                if(all_input[track]==1):
                    #print("impulse",all_input[track],track)
                    delta=UnitImpulse(lb,ub)
#                    print(delta[0],delta[1])
#                    signalDraw(delta[0],delta[1],"$\delta[n]$")
#                   
                 #unit step cheack
                elif(all_input[track]==2):
                    #print("unit step",all_input[track],track)
                    delta=UnitStep(lb,ub)
#                    print(delta[0],delta[1])
#                    signalDraw(delta[0],delta[1],"u[n]")
                    
                 #unit ramp cheack   
                elif(all_input[track]==3):
                    #print("unit ramp",all_input[track],track)
                    delta=UnitRamp(lb,ub)
#                    print(delta[0],delta[1])
#                    signalDraw(delta[0],delta[1],"ur[n]")
                delta=amplitude(delta,am)
#                print(delta)
                track=track+1 
                #shifting cheack
                if(all_input[track]==1):
                    #print("shifting has",all_input[track],track)
                    track=track+1 
                    #print("shifting amount",all_input[track],track)
                    shiftingAmount=all_input[track]
                    delta=timeshifting(delta,shiftingAmount)
#                    print(delta[0],delta[1])
#                    signalDraw(delta[0],delta[1],"shifting")
                   
                    
                else:
                    
                    print("no shifting amount",all_input[track])
                    
                 #mirroring cheack
                track=track+1
                if all_input[track]==1:
                    #print("mirroring",all_input[track],track)
                    delta= mirroring(delta)
#                    print(delta[0])
#                    signalDraw(delta[0],delta[1],"mirroring")
                     

                else:
                    
                    print("no mirroring",all_input[track])
                 
                #downsamling cheack
                track=track+1
                if all_input[track]==1:
                    
                    #print("downsamling",all_input[track],track) 
                    track=track+1 
                    dA=all_input[track]
                    delta=Downsampling(delta,dA)
                    
                else:
                    
                    print("no downsampling",all_input[track])
                 
                # cheack add,substract,multipliyer
                
                if signal==-1:
                    signal_p=delta
                else:
                    if signal==1:
#                       signalDraw(delta[0],delta[1],"1")
                       signal_p=Add(signal_p,delta)
#                       signalDraw(signal_p[0],signal_p[1],"1")
                    elif signal==2:
                       
                       #signalDraw(signal_p[0],signal_p[1],"1")
#                       signalDraw(delta[0],delta[1],"2")
                       signal_p=Subtract(signal_p,delta)
#                       signalDraw(signal_p[0],signal_p[1],"2")
                     
                    elif signal==3:
                       
                       signal_p=Multiply(signal_p,delta)
#                       signalDraw(signal_p[0],signal_p[1],"3")
                
                if signal_part>0:
                    track=track+1
                    signal=all_input[track]
                    
                    
            if comp==-1:
                comp_p=signal_p
            else:
                if comp==1:
#                   signalDraw(signal_p[0],signal_p[1],"1b")
                   comp_p=Add(comp_p,signal_p)
#                   signalDraw(comp_p[0],comp_p[1],"1A")
                     
                elif comp==2:
                     #print("sub",all_input[track],track)
                     #signalDraw(comp_p[0],comp_p[1],"1")
#                     signalDraw(signal_p[0],signal_p[1],"2B")
                     
                     comp_p=Subtract(comp_p,signal_p)
#                     signalDraw(comp_p[0],comp_p[1],"2A")
                     
                elif comp==3:
#                       signalDraw(signal_p[0],signal_p[1],"3")
                       comp_p=Multiply(comp_p,signal_p)
#                       signalDraw(comp_p[0],comp_p[1],"3")
              
            if comp_part>0:
               track=track+1
               comp=all_input[track]       
                
        print(comp_p[0],comp_p[1])           
        signalDraw(comp_p[0],comp_p[1],"final Result")
                 
                
            
        
        
         
                
                
                    
                        
                        
                        
                    
                
        
        
    
    