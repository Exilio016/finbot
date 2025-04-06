# BillUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_id** | **str** | Use either currency_id or currency_code | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code | [optional] 
**name** | **str** |  | 
**amount_min** | **str** |  | [optional] 
**amount_max** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**end_date** | **datetime** | The date after which this bill is no longer valid or applicable | [optional] 
**extension_date** | **datetime** | The date before which the bill must be renewed (or cancelled) | [optional] 
**repeat_freq** | [**BillRepeatFrequency**](BillRepeatFrequency.md) |  | [optional] 
**skip** | **int** | How often the bill must be skipped. 1 means a bi-monthly bill. | [optional] 
**active** | **bool** | If the bill is active. | [optional] 
**notes** | **str** |  | [optional] 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 

## Example

```python
from openapi_client.models.bill_update import BillUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BillUpdate from a JSON string
bill_update_instance = BillUpdate.from_json(json)
# print the JSON string representation of the object
print(BillUpdate.to_json())

# convert the object into a dict
bill_update_dict = bill_update_instance.to_dict()
# create an instance of BillUpdate from a dict
bill_update_from_dict = BillUpdate.from_dict(bill_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


