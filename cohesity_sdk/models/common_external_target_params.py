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
from cohesity_sdk.models.cloud_domain import CloudDomain
from typing import Optional, Set
from typing_extensions import Self

class CommonExternalTargetParams(BaseModel):
    """
    Specifies the parameters which are common between all External Target.
    """ # noqa: E501
    cloud_domains: Optional[List[CloudDomain]] = Field(default=None, description="Specifies the cloud domain information.", alias="cloudDomains")
    compression: Optional[StrictStr] = Field(default=None, description="Specifies whether the type of compression of the External Target")
    error_message: Optional[StrictStr] = Field(default=None, description="Specifies the error message if the event is in failed state.", alias="errorMessage")
    global_id: Optional[StrictStr] = Field(default=None, description="Specifies the global identifier of the External Target.", alias="globalId")
    id: Optional[StrictInt] = Field(default=None, description="Specifies the ID of the External Target.")
    is_worm_capable: Optional[StrictBool] = Field(default=None, description="Specifies whether this external target has been found to be capable of supporting WORM archives.", alias="isWormCapable")
    name: Optional[StrictStr] = Field(description="Specifies the name of the External Target.")
    ownership_context: Optional[StrictStr] = Field(default=None, description="Specifies whether how this external target is being consumed either Local or FortKnox.", alias="ownershipContext")
    purpose_type: Optional[StrictStr] = Field(description="Specifies the purpose of the External Target.", alias="purposeType")
    status: Optional[StrictStr] = Field(default=None, description="Specifies the registration status of the External Target")
    storage_domain_name: Optional[StrictStr] = Field(default=None, description="Specifies the storage domain associated with the target.", alias="storageDomainName")
    tenant_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies the list of tenantIds for the External Target", alias="tenantIds")
    __properties: ClassVar[List[str]] = ["cloudDomains", "compression", "errorMessage", "globalId", "id", "isWormCapable", "name", "ownershipContext", "purposeType", "status", "storageDomainName", "tenantIds"]

    @field_validator('compression')
    def compression_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['None', 'Low', 'High']):
            raise ValueError("must be one of enum values ('None', 'Low', 'High')")
        return value

    @field_validator('ownership_context')
    def ownership_context_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Local', 'FortKnox']):
            raise ValueError("must be one of enum values ('Local', 'FortKnox')")
        return value

    @field_validator('purpose_type')
    def purpose_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Archival', 'Tiering', 'Rpaas']):
            raise ValueError("must be one of enum values ('Archival', 'Tiering', 'Rpaas')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Registered', 'Unregistering', 'Unregistered']):
            raise ValueError("must be one of enum values ('Registered', 'Unregistering', 'Unregistered')")
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
        """Create an instance of CommonExternalTargetParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "error_message",
            "id",
            "status",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in cloud_domains (list)
        _items = []
        if self.cloud_domains:
            for _item_cloud_domains in self.cloud_domains:
                if _item_cloud_domains:
                    _items.append(_item_cloud_domains.to_dict())
            _dict['cloudDomains'] = _items
        # set to None if cloud_domains (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_domains is None and "cloud_domains" in self.model_fields_set:
            _dict['cloudDomains'] = None

        # set to None if compression (nullable) is None
        # and model_fields_set contains the field
        if self.compression is None and "compression" in self.model_fields_set:
            _dict['compression'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        # set to None if global_id (nullable) is None
        # and model_fields_set contains the field
        if self.global_id is None and "global_id" in self.model_fields_set:
            _dict['globalId'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if is_worm_capable (nullable) is None
        # and model_fields_set contains the field
        if self.is_worm_capable is None and "is_worm_capable" in self.model_fields_set:
            _dict['isWormCapable'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if ownership_context (nullable) is None
        # and model_fields_set contains the field
        if self.ownership_context is None and "ownership_context" in self.model_fields_set:
            _dict['ownershipContext'] = None

        # set to None if purpose_type (nullable) is None
        # and model_fields_set contains the field
        if self.purpose_type is None and "purpose_type" in self.model_fields_set:
            _dict['purposeType'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if storage_domain_name (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_name is None and "storage_domain_name" in self.model_fields_set:
            _dict['storageDomainName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonExternalTargetParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloudDomains": [CloudDomain.from_dict(_item) for _item in obj["cloudDomains"]] if obj.get("cloudDomains") is not None else None,
            "compression": obj.get("compression"),
            "errorMessage": obj.get("errorMessage"),
            "globalId": obj.get("globalId"),
            "id": obj.get("id"),
            "isWormCapable": obj.get("isWormCapable"),
            "name": obj.get("name"),
            "ownershipContext": obj.get("ownershipContext"),
            "purposeType": obj.get("purposeType"),
            "status": obj.get("status"),
            "storageDomainName": obj.get("storageDomainName"),
            "tenantIds": obj.get("tenantIds")
        })
        return _obj


