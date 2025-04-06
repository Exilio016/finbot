# PiggyBankUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**accounts** | [**List[PiggyBankAccountUpdate]**](PiggyBankAccountUpdate.md) |  | [optional] 
**currency_id** | **str** |  | [optional] [readonly] 
**currency_code** | **str** |  | [optional] [readonly] 
**target_amount** | **str** |  | [optional] 
**start_date** | **date** | The date you started with this piggy bank. | [optional] 
**target_date** | **date** | The date you intend to finish saving money. | [optional] 
**order** | **int** |  | [optional] 
**active** | **bool** |  | [optional] [readonly] 
**notes** | **str** |  | [optional] 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 

## Example

```python
from openapi_client.models.piggy_bank_update import PiggyBankUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankUpdate from a JSON string
piggy_bank_update_instance = PiggyBankUpdate.from_json(json)
# print the JSON string representation of the object
print(PiggyBankUpdate.to_json())

# convert the object into a dict
piggy_bank_update_dict = piggy_bank_update_instance.to_dict()
# create an instance of PiggyBankUpdate from a dict
piggy_bank_update_from_dict = PiggyBankUpdate.from_dict(piggy_bank_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


