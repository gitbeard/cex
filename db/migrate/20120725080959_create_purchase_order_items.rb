class CreatePurchaseOrderItems < ActiveRecord::Migration
  def change
    create_table :purchase_order_items do |t|
      t.integer :po_id
      t.integer :line_number
      t.integer :item_number
      t.integer :quantity
      t.float :unit_price
      t.float :extended_price

      t.timestamps
    end
  end
end
