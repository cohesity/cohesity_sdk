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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.helios.models.key_value_pair import KeyValuePair
from cohesity_sdk.helios.models.uda_source_registration_params_credentials import UdaSourceRegistrationParamsCredentials
from cohesity_sdk.helios.models.uda_source_registration_params_view_params import UdaSourceRegistrationParamsViewParams
from typing import Set
from typing_extensions import Self

class UdaSourceRegistrationParams(BaseModel):
    """
    Specifies parameters to register a Universal Data Adapter source.
    """ # noqa: E501
    credentials: Optional[UdaSourceRegistrationParamsCredentials] = None
    hosts: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="Specifies the IPs/hostnames for the nodes forming the Universal Data Adapter source cluster.")
    mount_view: Optional[StrictBool] = Field(default=None, description="Specifies if SMB/NFS view mounting should be enabled on source. Default value is false.", alias="mountView")
    os_type: Optional[StrictStr] = Field(default=None, description="Specifies the OS type for Universal Data Adapter source.", alias="osType")
    script_dir: StrictStr = Field(description="Specifies the absolute path of scripts used to interact with the Universal Data Adapter source.", alias="scriptDir")
    source_registration_args: Optional[StrictStr] = Field(default=None, description="Specifies custom arguments to be supplied to the source registration scripts. This field is deprecated. Use sourceRegistrationArguments instead.", alias="sourceRegistrationArgs")
    source_registration_arguments: Optional[List[KeyValuePair]] = Field(default=None, description="Specifies the map of custom arguments to be supplied to the source registration scripts.", alias="sourceRegistrationArguments")
    source_type: StrictStr = Field(description="Specifies the source type for Universal Data Adapter source.", alias="sourceType")
    view_params: Optional[UdaSourceRegistrationParamsViewParams] = Field(default=None, alias="viewParams")
    __properties: ClassVar[List[str]] = ["credentials", "hosts", "mountView", "osType", "scriptDir", "sourceRegistrationArgs", "sourceRegistrationArguments", "sourceType", "viewParams"]

    @field_validator('os_type')
    def os_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kLinux', 'kWindows', 'kAix']):
            raise ValueError("must be one of enum values ('kLinux', 'kWindows', 'kAix')")
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
        """Create an instance of UdaSourceRegistrationParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in source_registration_arguments (list)
        _items = []
        if self.source_registration_arguments:
            for _item_source_registration_arguments in self.source_registration_arguments:
                if _item_source_registration_arguments:
                    _items.append(_item_source_registration_arguments.to_dict())
            _dict['sourceRegistrationArguments'] = _items
        # override the default output from pydantic by calling `to_dict()` of view_params
        if self.view_params:
            _dict['viewParams'] = self.view_params.to_dict()
        # set to None if mount_view (nullable) is None
        # and model_fields_set contains the field
        if self.mount_view is None and "mount_view" in self.model_fields_set:
            _dict['mountView'] = None

        # set to None if os_type (nullable) is None
        # and model_fields_set contains the field
        if self.os_type is None and "os_type" in self.model_fields_set:
            _dict['osType'] = None

        # set to None if source_registration_args (nullable) is None
        # and model_fields_set contains the field
        if self.source_registration_args is None and "source_registration_args" in self.model_fields_set:
            _dict['sourceRegistrationArgs'] = None

        # set to None if source_registration_arguments (nullable) is None
        # and model_fields_set contains the field
        if self.source_registration_arguments is None and "source_registration_arguments" in self.model_fields_set:
            _dict['sourceRegistrationArguments'] = None

        # set to None if view_params (nullable) is None
        # and model_fields_set contains the field
        if self.view_params is None and "view_params" in self.model_fields_set:
            _dict['viewParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UdaSourceRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "credentials": UdaSourceRegistrationParamsCredentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "hosts": obj.get("hosts"),
            "mountView": obj.get("mountView"),
            "osType": obj.get("osType"),
            "scriptDir": obj.get("scriptDir"),
            "sourceRegistrationArgs": obj.get("sourceRegistrationArgs"),
            "sourceRegistrationArguments": [KeyValuePair.from_dict(_item) for _item in obj["sourceRegistrationArguments"]] if obj.get("sourceRegistrationArguments") is not None else None,
            "sourceType": obj.get("sourceType"),
            "viewParams": UdaSourceRegistrationParamsViewParams.from_dict(obj["viewParams"]) if obj.get("viewParams") is not None else None
        })
        return _obj


