from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        c_rate = request.POST.get('c_rate')
        bags = request.POST.get('bags')
        Ebag = request.POST.get('Ebag')
        # print(c_rate,bags)
        cost_per_each_bag = int(c_rate)*68/100
        total_cost = cost_per_each_bag*int(bags)
        empty_bag_cost = (int(bags)*int(Ebag))
        grand_total = total_cost - empty_bag_cost
        # print(f'Per bag ₹ :{cost_per_each_bag} and total cost :{total_cost} , after removal E bags {grand_total}')
        context = {'cost_per_bag': cost_per_each_bag,'total_cost':total_cost,'grand_total': grand_total,'bags':bags,'c_rate':c_rate,'Ebag': Ebag,'empty_bag_cost':empty_bag_cost}
        return render(request,'result.html',context)

    return render(request, 'home.html')



