from django.db import models

class IdsMap(models.Model):
    stock_id = models.CharField(db_column="stock_id", max_length=255, blank=False, null=False, primary_key=True)
    et_id = models.CharField(db_column="et_id", max_length=255, blank=False, null=False)

    class Meta :
        managed = True
        db_table = 'ids_map'
        ordering = ['stock_id']

class Sector(models.Model):
    stock_id = models.ForeignKey(db_column='stock_id',to=IdsMap, on_delete=models.CASCADE, primary_key=True)
    industry = models.CharField(db_column="industry", max_length=255, blank=False, null=False)
    sector = models.CharField(db_column="sector", max_length=255, blank=False, null=False)

    class Meta :
        managed = True
        db_table = 'sector'
        ordering = ['stock_id']

class Fundmental(models.Model):
    stock_id  = models.ForeignKey(db_column='stock_id',to=IdsMap ,on_delete=models.CASCADE, primary_key=True)
    mkt_cap = models.FloatField(db_column="mkt_cap", default=0.0)
    p_e = models.FloatField(db_column='p_e', null=True, blank=False,)
    p_b = models.FloatField(db_column='p_b', null=True, blank=False, )
    divd = models.FloatField(db_column='divd', null=True, blank=False, )
    f_v = models.FloatField(db_column='f_v', null=True, blank=False, )
    eps = models.FloatField(db_column='eps', null=True, blank=False, )
    bv_sh = models.FloatField(db_column='bv_sh', null=True, blank=False, )

    class Meta :
        managed = True
        db_table = 'fundamental'
        ordering = ['stock_id']

class BalanceSheet(models.Model):
    id = models.AutoField(primary_key = True)
    stock_id = models.ForeignKey(db_column='stock_id', to=IdsMap, on_delete=models.CASCADE, default='XXXX')
    year = models.DateField(db_column='year')
    net_worth = models.FloatField(db_column='net_worth', blank=False, null=False)
    total_liabilities = models.FloatField(db_column='total_liabilities', blank=False, null=False, )
    total_current_assests = models.FloatField(db_column='total_current_assests', blank=False, null=False,)
    net_current_assets = models.FloatField(db_column='net_current_assets', blank=False, null=False, )
    total_assets = models.FloatField(db_column='total_assets', blank=False, null=False, )

    class Meta:
        managed = True
        db_table = 'balance_sheet'
        ordering = ['stock_id']
