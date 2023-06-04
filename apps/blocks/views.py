from django.shortcuts import render,redirect
from .models import Block
from django.contrib.auth.decorators import login_required
from .forms import BlockForm
from django.contrib import messages
import xlwt
from django.http import HttpResponse

@login_required(login_url='userLogin')
def index(request):
    objs = Block.objects.all()

    context = {
        "results":objs,
    }
    return render(request,"blocks/index.html",context)


@login_required(login_url='userLogin')
def addBlock(request):
    if request.method == "POST":
        form = BlockForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save()
            blockObj = Block.objects.filter(id=instance.id).first()
            if blockObj:
                blockObj.cbm =float((float(blockObj.block_height)*float(blockObj.block_length)*float(blockObj.block_width))/1000000)
                blockObj.measurement_weight = float(float(blockObj.cbm)*2.72)
                blockObj.save()
            messages.success(request, 'Block addedd successfully')
            return redirect("block.index")
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = BlockForm()

    context = {
        "form": form
    }
    return render(request,"blocks/add.html",context)

# @login_required(login_url='userLogin')
# def editCategory(request,id,slug):
#     categoryObj = Category.objects.filter(id=id,slug__iexact = slug).first()
#     if request.method == "POST":
#         form = CategoryForm(request.POST,instance=categoryObj)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Category update successfully')
#             return redirect("category.index")
#         else:
#             for field in form.errors:
#                 form[field].field.widget.attrs['class'] += ' is-invalid'
#     else:
#         form = CategoryForm(instance=categoryObj)

#     context = {
#         "form": form,
#         "data":categoryObj
#     }
#     return render(request,"category/edit.html",context)


@login_required(login_url='userLogin')
def deleteBlock(request,id):
    blockObj = Block.objects.filter(id=id).first()
    if blockObj:
        blockObj.delete()
        messages.success(request, 'Block deleted successfully')
        return redirect("block.index")
    else:
        return redirect("block.index")



@login_required(login_url='userLogin')
def export_block_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="blocks.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Block Number', 'Person Name', 'Bench Number', 'Block Length','Block Height','Block Width','varient' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Block.objects.all().values_list('block_number', 'name_of_person','bench_number', 'block_length', 'block_height','block_width','verient')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response