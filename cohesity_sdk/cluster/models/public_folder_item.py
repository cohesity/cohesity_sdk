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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.object_summary import ObjectSummary
from cohesity_sdk.cluster.models.snapshot_tag_info import SnapshotTagInfo
from cohesity_sdk.cluster.models.tag_info import TagInfo
from typing import Set
from typing_extensions import Self

class PublicFolderItem(BaseModel):
    """
    Specifies an Public folder indexed item.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the object.")
    path: Optional[StrictStr] = Field(default=None, description="Specifies the path of the object.")
    policy_id: Optional[StrictStr] = Field(default=None, description="Specifies the protection policy id for this file.", alias="policyId")
    policy_name: Optional[StrictStr] = Field(default=None, description="Specifies the protection policy name for this file.", alias="policyName")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="\"Specifies the protection group id which contains this object.\"", alias="protectionGroupId")
    protection_group_name: Optional[StrictStr] = Field(default=None, description="\"Specifies the protection group name which contains this object.\"", alias="protectionGroupName")
    source_info: Optional[ObjectSummary] = Field(default=None, alias="sourceInfo")
    storage_domain_id: Optional[StrictInt] = Field(default=None, description="\"Specifies the Storage Domain id where the backup data of Object is present.\"", alias="storageDomainId")
    snapshot_tags: Optional[List[SnapshotTagInfo]] = Field(default=None, description="Specifies snapshot tags applied to the object.", alias="snapshotTags")
    tags: Optional[List[TagInfo]] = Field(default=None, description="Specifies tag applied to the object.")
    has_attachments: Optional[StrictBool] = Field(default=None, description="Specifies whether the item has any attachments", alias="hasAttachments")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the id of the indexed item.")
    item_class: Optional[StrictStr] = Field(default=None, description="Specifies the item class of the indexed item.", alias="itemClass")
    item_size: Optional[StrictInt] = Field(default=None, description="Specifies the size in bytes for the indexed item.", alias="itemSize")
    parent_folder_id: Optional[StrictStr] = Field(default=None, description="Specifies the id of parent folder the indexed item.", alias="parentFolderId")
    received_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the Unix timestamp epoch in seconds at which this item is received.", alias="receivedTimeSecs")
    subject: Optional[StrictStr] = Field(default=None, description="Specifies the subject of the indexed item.")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the Public folder item type.")
    __properties: ClassVar[List[str]] = ["name", "path", "policyId", "policyName", "protectionGroupId", "protectionGroupName", "sourceInfo", "storageDomainId", "snapshotTags", "tags", "hasAttachments", "id", "itemClass", "itemSize", "parentFolderId", "receivedTimeSecs", "subject", "type"]

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
        """Create an instance of PublicFolderItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source_info
        if self.source_info:
            _dict['sourceInfo'] = self.source_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in snapshot_tags (list)
        _items = []
        if self.snapshot_tags:
            for _item_snapshot_tags in self.snapshot_tags:
                if _item_snapshot_tags:
                    _items.append(_item_snapshot_tags.to_dict())
            _dict['snapshotTags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.policy_id is None and "policy_id" in self.model_fields_set:
            _dict['policyId'] = None

        # set to None if policy_name (nullable) is None
        # and model_fields_set contains the field
        if self.policy_name is None and "policy_name" in self.model_fields_set:
            _dict['policyName'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if protection_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_name is None and "protection_group_name" in self.model_fields_set:
            _dict['protectionGroupName'] = None

        # set to None if storage_domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_id is None and "storage_domain_id" in self.model_fields_set:
            _dict['storageDomainId'] = None

        # set to None if snapshot_tags (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_tags is None and "snapshot_tags" in self.model_fields_set:
            _dict['snapshotTags'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if has_attachments (nullable) is None
        # and model_fields_set contains the field
        if self.has_attachments is None and "has_attachments" in self.model_fields_set:
            _dict['hasAttachments'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if item_class (nullable) is None
        # and model_fields_set contains the field
        if self.item_class is None and "item_class" in self.model_fields_set:
            _dict['itemClass'] = None

        # set to None if item_size (nullable) is None
        # and model_fields_set contains the field
        if self.item_size is None and "item_size" in self.model_fields_set:
            _dict['itemSize'] = None

        # set to None if parent_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_folder_id is None and "parent_folder_id" in self.model_fields_set:
            _dict['parentFolderId'] = None

        # set to None if received_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.received_time_secs is None and "received_time_secs" in self.model_fields_set:
            _dict['receivedTimeSecs'] = None

        # set to None if subject (nullable) is None
        # and model_fields_set contains the field
        if self.subject is None and "subject" in self.model_fields_set:
            _dict['subject'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicFolderItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "path": obj.get("path"),
            "policyId": obj.get("policyId"),
            "policyName": obj.get("policyName"),
            "protectionGroupId": obj.get("protectionGroupId"),
            "protectionGroupName": obj.get("protectionGroupName"),
            "sourceInfo": ObjectSummary.from_dict(obj["sourceInfo"]) if obj.get("sourceInfo") is not None else None,
            "storageDomainId": obj.get("storageDomainId"),
            "snapshotTags": [SnapshotTagInfo.from_dict(_item) for _item in obj["snapshotTags"]] if obj.get("snapshotTags") is not None else None,
            "tags": [TagInfo.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "hasAttachments": obj.get("hasAttachments"),
            "id": obj.get("id"),
            "itemClass": obj.get("itemClass"),
            "itemSize": obj.get("itemSize"),
            "parentFolderId": obj.get("parentFolderId"),
            "receivedTimeSecs": obj.get("receivedTimeSecs"),
            "subject": obj.get("subject"),
            "type": obj.get("type")
        })
        return _obj


