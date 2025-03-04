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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.azure_target_params_for_recover_vm import AzureTargetParamsForRecoverVm
from cohesity_sdk.models.recover_protection_group_run_params import RecoverProtectionGroupRunParams
from typing import Optional, Set
from typing_extensions import Self

class RecoverAzureVmParams(BaseModel):
    """
    Specifies the parameters to recover Azure VM.
    """ # noqa: E501
    azure_target_params: Optional[AzureTargetParamsForRecoverVm] = Field(default=None, alias="azureTargetParams")
    recover_protection_group_runs_params: Optional[List[RecoverProtectionGroupRunParams]] = Field(default=None, description="Specifies the Protection Group Runs params to recover. All the VM's that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of VMs. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object's snapshot.", alias="recoverProtectionGroupRunsParams")
    target_environment: StrictStr = Field(description="Specifies the environment of the recovery target. The corresponding params below must be filled out.", alias="targetEnvironment")
    __properties: ClassVar[List[str]] = ["azureTargetParams", "recoverProtectionGroupRunsParams", "targetEnvironment"]

    @field_validator('target_environment')
    def target_environment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['kAzure']):
            raise ValueError("must be one of enum values ('kAzure')")
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
        """Create an instance of RecoverAzureVmParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of azure_target_params
        if self.azure_target_params:
            _dict['azureTargetParams'] = self.azure_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in recover_protection_group_runs_params (list)
        _items = []
        if self.recover_protection_group_runs_params:
            for _item_recover_protection_group_runs_params in self.recover_protection_group_runs_params:
                if _item_recover_protection_group_runs_params:
                    _items.append(_item_recover_protection_group_runs_params.to_dict())
            _dict['recoverProtectionGroupRunsParams'] = _items
        # set to None if recover_protection_group_runs_params (nullable) is None
        # and model_fields_set contains the field
        if self.recover_protection_group_runs_params is None and "recover_protection_group_runs_params" in self.model_fields_set:
            _dict['recoverProtectionGroupRunsParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverAzureVmParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "azureTargetParams": AzureTargetParamsForRecoverVm.from_dict(obj["azureTargetParams"]) if obj.get("azureTargetParams") is not None else None,
            "recoverProtectionGroupRunsParams": [RecoverProtectionGroupRunParams.from_dict(_item) for _item in obj["recoverProtectionGroupRunsParams"]] if obj.get("recoverProtectionGroupRunsParams") is not None else None,
            "targetEnvironment": obj.get("targetEnvironment")
        })
        return _obj


