from django.http import JsonResponse, HttpResponseBadRequest
from erp_system.models.manager2 import warehouse_product
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import permission_required


@api_view(['POST'])
@swagger_auto_schema(operation_description="Admin replenish stock for a warehouse product")
@permission_required('erp_system.change_warehouse_product', raise_exception=True)
def admin_replenish_stock(request, warehouse_product_id, count):
    try:
        product = warehouse_product.objects.get(id=warehouse_product_id)
        product.increase_stock(count)

        return JsonResponse({'status':'success', 'message':f'Successfully replenished {count} of {product.name}'})

    except warehouse_product_id.DoesNotExist:
        return JsonResponse({'status':'fail', 'message':'Product does not exist'}, status=400)

    except ValueError:
        return HttpResponseBadRequest('Invalid input')


