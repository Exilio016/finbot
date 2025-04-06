# BillStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_id** | **str** | Use either currency_id or currency_code | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code | [optional] 
**name** | **str** |  | 
**amount_min** | **str** |  | 
**amount_max** | **str** |  | 
**var_date** | **datetime** |  | 
**end_date** | **datetime** | The date after which this bill is no longer valid or applicable | [optional] 
**extension_date** | **datetime** | The date before which the bill must be renewed (or cancelled) | [optional] 
**repeat_freq** | [**BillRepeatFrequency**](BillRepeatFrequency.md) |  | 
**skip** | **int** | How often the bill must be skipped. 1 means a bi-monthly bill. | [optional] 
**active** | **bool** | If the bill is active. | [optional] 
**notes** | **str** |  | [optional] 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 

## Example

```python
from openapi_client.models.bill_store import BillStore

# TODO update the JSON string below
json = "{}"
# create an instance of BillStore from a JSON string
bill_store_instance = BillStore.from_json(json)
# print the JSON string representation of the object
print(BillStore.to_json())

# convert the object into a dict
bill_store_dict = bill_store_instance.to_dict()
# create an instance of BillStore from a dict
bill_store_from_dict = BillStore.from_dict(bill_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


