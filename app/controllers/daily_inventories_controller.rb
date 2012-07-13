class DailyInventoriesController < ApplicationController
  # GET /daily_inventories
  # GET /daily_inventories.json
  def index
    @daily_inventories = DailyInventory.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @daily_inventories }
    end
  end

  # GET /daily_inventories/1
  # GET /daily_inventories/1.json
  def show
    @daily_inventory = DailyInventory.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @daily_inventory }
    end
  end

  # GET /daily_inventories/new
  # GET /daily_inventories/new.json
  def new
    @daily_inventory = DailyInventory.new

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @daily_inventory }
    end
  end

  # GET /daily_inventories/1/edit
  def edit
    @daily_inventory = DailyInventory.find(params[:id])
  end

  # POST /daily_inventories
  # POST /daily_inventories.json
  def create
    @daily_inventory = DailyInventory.new(params[:daily_inventory])

    respond_to do |format|
      if @daily_inventory.save
        format.html { redirect_to @daily_inventory, notice: 'Daily inventory was successfully created.' }
        format.json { render json: @daily_inventory, status: :created, location: @daily_inventory }
      else
        format.html { render action: "new" }
        format.json { render json: @daily_inventory.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /daily_inventories/1
  # PUT /daily_inventories/1.json
  def update
    @daily_inventory = DailyInventory.find(params[:id])

    respond_to do |format|
      if @daily_inventory.update_attributes(params[:daily_inventory])
        format.html { redirect_to @daily_inventory, notice: 'Daily inventory was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @daily_inventory.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /daily_inventories/1
  # DELETE /daily_inventories/1.json
  def destroy
    @daily_inventory = DailyInventory.find(params[:id])
    @daily_inventory.destroy

    respond_to do |format|
      format.html { redirect_to daily_inventories_url }
      format.json { head :no_content }
    end
  end
end
