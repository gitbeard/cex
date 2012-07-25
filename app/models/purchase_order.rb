class PurchaseOrder < ActiveRecord::Base
  attr_accessible :company_id, :date_placed, :date_ready, :date_received, :date_shipped, :po_number
end
