class PurchaseOrderItem < ActiveRecord::Base
  attr_accessible :extended_price, :item_number, :line_number, :po_id, :quantity, :unit_price
end
