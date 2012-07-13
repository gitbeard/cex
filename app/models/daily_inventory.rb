class DailyInventory < ActiveRecord::Base
  attr_accessible :datetime, :file_id, :item_number, :location_id, :quantity
  
  belongs_to :item
end
