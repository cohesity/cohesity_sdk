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
from cohesity_sdk.helios.models.azure_object_level_params import AzureObjectLevelParams
from cohesity_sdk.helios.models.azure_sql_package_options import AzureSqlPackageOptions
from cohesity_sdk.helios.models.azure_sql_sku_options import AzureSqlSkuOptions
from typing import Set
from typing_extensions import Self

class AzureSqlObjectProtectionParams(BaseModel):
    """
    Specifies the parameters which are specific to Azure SQL Object Protection Groups using Azure native APIs. Atlease one of objects must be specified.
    """ # noqa: E501
    copy_database: Optional[StrictBool] = Field(default=None, description="If set to true, a copy of the database is created during backup, and the backup is performed from the copied database. This backup will be transactionally consistent. If set to false, the backup is performed from the production database while transactions are in progress. In this case, the backup will be transactionally inconsistent, and recovery can fail or the recovered database may be in an inconsistent state.", alias="copyDatabase")
    copy_database_sku: Optional[AzureSqlSkuOptions] = Field(default=None, alias="copyDatabaseSku")
    disk_type: Optional[StrictStr] = Field(default=None, description="Specifies azure managed storage disk to be used for object protection. By default Premium LRS is being used to support Azure SQL workloads.", alias="diskType")
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the ids of the objects to be excluded in the Object Protection. This can be used to ignore specific objects under a parent object which has been included for protection.", alias="excludeObjectIds")
    objects: Optional[List[AzureObjectLevelParams]] = Field(default=None, description="Specifies the objects to be protected.")
    sql_package_options: Optional[AzureSqlPackageOptions] = Field(default=None, alias="sqlPackageOptions")
    temp_disk_size_gb: Optional[StrictInt] = Field(default=None, description="Specifies the size of the disk we will attach to rigel to use for exporting this DB(in GB).", alias="tempDiskSizeGb")
    __properties: ClassVar[List[str]] = ["copyDatabase", "copyDatabaseSku", "diskType", "excludeObjectIds", "objects", "sqlPackageOptions", "tempDiskSizeGb"]

    @field_validator('disk_type')
    def disk_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PremiumSSD', 'PremiumSSDv2', 'StandardSSD', 'StandardHDD', 'UltraDisk', 'Premium_LRS', 'PremiumV2_LRS', 'Premium_ZRS', 'StandardSSD_LRS', 'StandardSSD_ZRS', 'Standard_LRS', 'UltraSSD_LRS']):
            raise ValueError("must be one of enum values ('PremiumSSD', 'PremiumSSDv2', 'StandardSSD', 'StandardHDD', 'UltraDisk', 'Premium_LRS', 'PremiumV2_LRS', 'Premium_ZRS', 'StandardSSD_LRS', 'StandardSSD_ZRS', 'Standard_LRS', 'UltraSSD_LRS')")
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
        """Create an instance of AzureSqlObjectProtectionParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of copy_database_sku
        if self.copy_database_sku:
            _dict['copyDatabaseSku'] = self.copy_database_sku.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of sql_package_options
        if self.sql_package_options:
            _dict['sqlPackageOptions'] = self.sql_package_options.to_dict()
        # set to None if copy_database (nullable) is None
        # and model_fields_set contains the field
        if self.copy_database is None and "copy_database" in self.model_fields_set:
            _dict['copyDatabase'] = None

        # set to None if disk_type (nullable) is None
        # and model_fields_set contains the field
        if self.disk_type is None and "disk_type" in self.model_fields_set:
            _dict['diskType'] = None

        # set to None if exclude_object_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_object_ids is None and "exclude_object_ids" in self.model_fields_set:
            _dict['excludeObjectIds'] = None

        # set to None if temp_disk_size_gb (nullable) is None
        # and model_fields_set contains the field
        if self.temp_disk_size_gb is None and "temp_disk_size_gb" in self.model_fields_set:
            _dict['tempDiskSizeGb'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureSqlObjectProtectionParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "copyDatabase": obj.get("copyDatabase"),
            "copyDatabaseSku": AzureSqlSkuOptions.from_dict(obj["copyDatabaseSku"]) if obj.get("copyDatabaseSku") is not None else None,
            "diskType": obj.get("diskType"),
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "objects": [AzureObjectLevelParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "sqlPackageOptions": AzureSqlPackageOptions.from_dict(obj["sqlPackageOptions"]) if obj.get("sqlPackageOptions") is not None else None,
            "tempDiskSizeGb": obj.get("tempDiskSizeGb")
        })
        return _obj


