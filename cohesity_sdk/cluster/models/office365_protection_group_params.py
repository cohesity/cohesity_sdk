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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.cluster.models.indexing_policy import IndexingPolicy
from cohesity_sdk.cluster.models.office365_one_drive_protection_group_params import Office365OneDriveProtectionGroupParams
from cohesity_sdk.cluster.models.office365_outlook_protection_group_params import Office365OutlookProtectionGroupParams
from cohesity_sdk.cluster.models.office365_protection_group_object_params import Office365ProtectionGroupObjectParams
from cohesity_sdk.cluster.models.office365_public_folders_protection_group_params import Office365PublicFoldersProtectionGroupParams
from cohesity_sdk.cluster.models.office365_share_point_protection_group_params import Office365SharePointProtectionGroupParams
from typing import Set
from typing_extensions import Self

class Office365ProtectionGroupParams(BaseModel):
    """
    Specifies the parameters which are specific to Office 365 related Protection Groups.
    """ # noqa: E501
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the objects to be excluded in the Protection Group.", alias="excludeObjectIds")
    indexing_policy: Optional[IndexingPolicy] = Field(default=None, alias="indexingPolicy")
    objects: Annotated[List[Office365ProtectionGroupObjectParams], Field(min_length=1)] = Field(description="Specifies the objects to be included in the Protection Group.")
    one_drive_protection_type_params: Optional[Office365OneDriveProtectionGroupParams] = Field(default=None, alias="oneDriveProtectionTypeParams")
    outlook_protection_type_params: Optional[Office365OutlookProtectionGroupParams] = Field(default=None, alias="outlookProtectionTypeParams")
    protection_types: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="Specifies the Office 365 Protection Group types.", alias="protectionTypes")
    public_folders_protection_type_params: Optional[Office365PublicFoldersProtectionGroupParams] = Field(default=None, alias="publicFoldersProtectionTypeParams")
    share_point_protection_type_params: Optional[Office365SharePointProtectionGroupParams] = Field(default=None, alias="sharePointProtectionTypeParams")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the parent of the objects.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the parent of the objects.", alias="sourceName")
    __properties: ClassVar[List[str]] = ["excludeObjectIds", "indexingPolicy", "objects", "oneDriveProtectionTypeParams", "outlookProtectionTypeParams", "protectionTypes", "publicFoldersProtectionTypeParams", "sharePointProtectionTypeParams", "sourceId", "sourceName"]

    @field_validator('protection_types')
    def protection_types_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['kMailbox', 'kOneDrive', 'kSharePoint', 'kPublicFolders', 'kGroups', 'kTeams']):
                raise ValueError("each list item must be one of ('kMailbox', 'kOneDrive', 'kSharePoint', 'kPublicFolders', 'kGroups', 'kTeams')")
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
        """Create an instance of Office365ProtectionGroupParams from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "source_id",
            "source_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of indexing_policy
        if self.indexing_policy:
            _dict['indexingPolicy'] = self.indexing_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of one_drive_protection_type_params
        if self.one_drive_protection_type_params:
            _dict['oneDriveProtectionTypeParams'] = self.one_drive_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outlook_protection_type_params
        if self.outlook_protection_type_params:
            _dict['outlookProtectionTypeParams'] = self.outlook_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public_folders_protection_type_params
        if self.public_folders_protection_type_params:
            _dict['publicFoldersProtectionTypeParams'] = self.public_folders_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of share_point_protection_type_params
        if self.share_point_protection_type_params:
            _dict['sharePointProtectionTypeParams'] = self.share_point_protection_type_params.to_dict()
        # set to None if exclude_object_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_object_ids is None and "exclude_object_ids" in self.model_fields_set:
            _dict['excludeObjectIds'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if source_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_name is None and "source_name" in self.model_fields_set:
            _dict['sourceName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Office365ProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "indexingPolicy": IndexingPolicy.from_dict(obj["indexingPolicy"]) if obj.get("indexingPolicy") is not None else None,
            "objects": [Office365ProtectionGroupObjectParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "oneDriveProtectionTypeParams": Office365OneDriveProtectionGroupParams.from_dict(obj["oneDriveProtectionTypeParams"]) if obj.get("oneDriveProtectionTypeParams") is not None else None,
            "outlookProtectionTypeParams": Office365OutlookProtectionGroupParams.from_dict(obj["outlookProtectionTypeParams"]) if obj.get("outlookProtectionTypeParams") is not None else None,
            "protectionTypes": obj.get("protectionTypes"),
            "publicFoldersProtectionTypeParams": Office365PublicFoldersProtectionGroupParams.from_dict(obj["publicFoldersProtectionTypeParams"]) if obj.get("publicFoldersProtectionTypeParams") is not None else None,
            "sharePointProtectionTypeParams": Office365SharePointProtectionGroupParams.from_dict(obj["sharePointProtectionTypeParams"]) if obj.get("sharePointProtectionTypeParams") is not None else None,
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName")
        })
        return _obj


