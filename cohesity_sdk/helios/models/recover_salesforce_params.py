# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.common_recover_object_snapshot_params import CommonRecoverObjectSnapshotParams
from cohesity_sdk.helios.models.recover_sfdc_object_params import RecoverSfdcObjectParams
from typing import Set
from typing_extensions import Self

class RecoverSalesforceParams(BaseModel):
    """
    Specifies the recovery options specific to Salesforce environment.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other salesforce objects if one of Object failed to recover. Default value is false.", alias="continueOnError")
    objects: Optional[List[CommonRecoverObjectSnapshotParams]] = Field(description="Specifies the list of recover Object parameters.")
    recover_sfdc_object_params: Optional[RecoverSfdcObjectParams] = Field(default=None, alias="recoverSfdcObjectParams")
    recover_to: Optional[StrictInt] = Field(default=None, description="Specifies the id of registered source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location.", alias="recoverTo")
    recovery_action: StrictStr = Field(description="Specifies the type of recover action to be performed.", alias="recoveryAction")
    __properties: ClassVar[List[str]] = ["continueOnError", "objects", "recoverSfdcObjectParams", "recoverTo", "recoveryAction"]

    @field_validator('recovery_action')
    def recovery_action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RecoverSfdcObjects', 'RecoverSfdcOrg', 'RecoverSfdcRecords']):
            raise ValueError("must be one of enum values ('RecoverSfdcObjects', 'RecoverSfdcOrg', 'RecoverSfdcRecords')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RecoverSalesforceParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of recover_sfdc_object_params
        if self.recover_sfdc_object_params:
            _dict['recoverSfdcObjectParams'] = self.recover_sfdc_object_params.to_dict()
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        # set to None if recover_to (nullable) is None
        # and model_fields_set contains the field
        if self.recover_to is None and "recover_to" in self.model_fields_set:
            _dict['recoverTo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverSalesforceParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "objects": [CommonRecoverObjectSnapshotParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "recoverSfdcObjectParams": RecoverSfdcObjectParams.from_dict(obj["recoverSfdcObjectParams"]) if obj.get("recoverSfdcObjectParams") is not None else None,
            "recoverTo": obj.get("recoverTo"),
            "recoveryAction": obj.get("recoveryAction")
        })
        return _obj


