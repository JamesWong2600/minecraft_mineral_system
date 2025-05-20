package mineralindication.mineralindication;

import org.bukkit.ChatColor;
import org.bukkit.Material;
import org.bukkit.Sound;
import org.bukkit.block.Block;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.block.BlockBreakEvent;
import org.bukkit.event.player.PlayerMoveEvent;

import java.sql.*;
import java.util.Random;
import java.util.UUID;

public class mineralshow implements Listener {
    int x= 0;
    static final String mineral = "SELECT id, iron, coal, diamond FROM mineral";


    Random random = new Random();
    @EventHandler
    public void onBlockBreak(BlockBreakEvent event) {
        Player p = event.getPlayer();
        UUID UUid = p.getUniqueId();
        String uid = String.valueOf(UUid);
        Random random = new Random();
        String ID = String.valueOf(p);
        String q1 = "CraftPlayer{name=";
        String q2 = "}";
        Block block = event.getBlock();
        String q3 = ID.replace(q1, "").replace(q2, "");
        String ip = Mineralindication.getMain().getConfig().getString("SQL.ip");
        String table = Mineralindication.getMain().getConfig().getString("SQL.table");
        String user = Mineralindication.getMain().getConfig().getString("SQL.user");
        String password = Mineralindication.getMain().getConfig().getString("SQL.password");
        String DB_DRIVER = "com.mysql.jdbc.Driver";
        String DB_URL = "jdbc:mysql://" + ip + "/" + table;
        String DB_USERNAME = user;
        String DB_PASSWORD = password;
        try(Connection conn1 = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
            Statement stmt1 = conn1.createStatement();
            Statement stmt2 = conn1.createStatement();
            ResultSet rs = stmt2.executeQuery("SELECT * FROM usermineral");
        ) {
            while(rs.next()) {
            String PLAYERUUID = rs.getString("UUID");
            System.out.println(PLAYERUUID);
            System.out.println(UUid);
            if(uid.equals(PLAYERUUID)){
            x=1;
        }}
            if(x==0){
                p.sendMessage(ChatColor.RED + "YOU NEED TO CREATE AN BANK ACCOUNT FIRST BEFORE YOU MINING，BY USING COMMAND/register <USERNAME> <PASSWORD>");
                event.setCancelled(true);
                p.playSound(p.getLocation(), Sound.ENTITY_EXPERIENCE_ORB_PICKUP, 20, 1);
            }
            if(x==1){
                if (block.getType() == Material.DIAMOND_ORE || block.getType() == Material.DEEPSLATE_DIAMOND_ORE){
                    try(Connection conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
                        Statement stmt4 = conn.createStatement();
                        Statement stmt5 = conn.createStatement()
                    ) {
                        String sqldata = "UPDATE mineral " +
                                "SET diamond = diamond + 1 WHERE id in (0)";
                        stmt4.executeUpdate(sqldata);
                        String sqldata1 = "UPDATE usermineral " +
                                "SET diamond = diamond + 1 WHERE UUID in ('"+UUid+"')";
                        stmt5.executeUpdate(sqldata1);
                        p.sendMessage(ChatColor.GREEN + "diamond+1");
                        p.playSound(p.getLocation(), Sound.ENTITY_EXPERIENCE_ORB_PICKUP, 20, 1);
                        event.setCancelled(true);
                        block.setType(Material.AIR);
                    }
                    catch (SQLException ed) {
                        ed.printStackTrace();

                    }
                }
                if (block.getType() == Material.IRON_ORE || block.getType() == Material.DEEPSLATE_IRON_ORE){

                    try(Connection conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
                        Statement stmt4 = conn.createStatement();
                        Statement stmt5 = conn.createStatement()
                    ) {
                        String sqldata = "UPDATE mineral " +
                                "SET iron = iron + 1 WHERE id in (0)";
                        stmt4.executeUpdate(sqldata);
                        String sqldata1 = "UPDATE usermineral " +
                                "SET iron = iron + 1 WHERE UUID in ('"+UUid+"')";
                        stmt5.executeUpdate(sqldata1);
                        p.sendMessage(ChatColor.GREEN + "iron+1");
                        p.playSound(p.getLocation(), Sound.ENTITY_EXPERIENCE_ORB_PICKUP, 20, 1);
                        event.setCancelled(true);
                        block.setType(Material.AIR);
                    }
                    catch (SQLException ed) {
                        ed.printStackTrace();

                    }

                }
                if (block.getType() == Material.COAL_ORE || block.getType() == Material.DEEPSLATE_COAL_ORE){

                    try(Connection conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
                        Statement stmt4 = conn.createStatement();
                        Statement stmt5 = conn.createStatement()
                    ) {
                        String sqldata = "UPDATE mineral " +
                                "SET coal = coal + 1 WHERE id in (0)";
                        String sqldata1 = "UPDATE usermineral " +
                                "SET coal = coal + 1 WHERE UUID in ('"+UUid+"')";
                        stmt4.executeUpdate(sqldata1);
                        p.sendMessage(ChatColor.GREEN + "coal+1");
                        p.playSound(p.getLocation(), Sound.ENTITY_EXPERIENCE_ORB_PICKUP, 20, 1);
                        stmt5.executeUpdate(sqldata1);
                        event.setCancelled(true);
                        block.setType(Material.AIR);
                    }
                    catch (SQLException ed) {
                        ed.printStackTrace();

                    }

                }

                if (block.getType() == Material.GOLD_ORE || block.getType() == Material.DEEPSLATE_GOLD_ORE){

                    try(Connection conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
                        Statement stmt4 = conn.createStatement();
                        Statement stmt5 = conn.createStatement()
                    ) {
                        String sqldata = "UPDATE mineral " +
                                "SET gold = gold + 1 WHERE id in (0)";
                        stmt4.executeUpdate(sqldata);
                        String sqldata1 = "UPDATE usermineral " +
                                "SET gold = gold + 1 WHERE UUID in ('"+UUid+"')";
                        stmt5.executeUpdate(sqldata1);
                        p.sendMessage(ChatColor.GREEN + "gold+1");
                        p.playSound(p.getLocation(), Sound.ENTITY_EXPERIENCE_ORB_PICKUP, 20, 1);
                        event.setCancelled(true);
                        block.setType(Material.AIR);
                    }
                    catch (SQLException ed) {
                        ed.printStackTrace();

                    }

                }
                if (block.getType() == Material.EMERALD_ORE || block.getType() == Material.DEEPSLATE_EMERALD_ORE){

                    try(Connection conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
                        Statement stmt4 = conn.createStatement();
                        Statement stmt5 = conn.createStatement()
                    ) {
                        String sqldata = "UPDATE mineral " +
                                "SET emerald = emerald + 1 WHERE id in (0)";
                        stmt4.executeUpdate(sqldata);
                        String sqldata1 = "UPDATE usermineral " +
                                "SET emerald = emerald + 1 WHERE UUID in ('"+UUid+"')";
                        stmt5.executeUpdate(sqldata1);
                        p.sendMessage(ChatColor.GREEN + "emerald+1");
                        p.playSound(p.getLocation(), Sound.ENTITY_EXPERIENCE_ORB_PICKUP, 20, 1);
                        event.setCancelled(true);
                        block.setType(Material.AIR);
                    }
                    catch (SQLException ed) {
                        ed.printStackTrace();

                    }

                }
                if (block.getType() == Material.COPPER_ORE || block.getType() == Material.DEEPSLATE_COPPER_ORE){

                    try(Connection conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
                        Statement stmt4 = conn.createStatement();
                        Statement stmt5 = conn.createStatement()
                    ) {
                        String sqldata = "UPDATE mineral " +
                                "SET copper = copper + 1 WHERE id in (0)";
                        stmt4.executeUpdate(sqldata);
                        String sqldata1 = "UPDATE usermineral " +
                                "SET copper = copper + 1 WHERE UUID in ('"+UUid+"')";
                        stmt5.executeUpdate(sqldata1);
                        p.sendMessage(ChatColor.GREEN + "copper+1");
                        p.playSound(p.getLocation(), Sound.ENTITY_EXPERIENCE_ORB_PICKUP, 20, 1);
                        event.setCancelled(true);
                        block.setType(Material.AIR);
                    }
                    catch (SQLException ed) {
                        ed.printStackTrace();

                    }

                }
                if (block.getType() == Material.REDSTONE_ORE || block.getType() == Material.DEEPSLATE_REDSTONE_ORE){

                    try(Connection conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
                        Statement stmt4 = conn.createStatement();
                        Statement stmt5 = conn.createStatement()
                    ) {
                        String sqldata = "UPDATE mineral " +
                                "SET redstone = redstone + 1 WHERE id in (0)";
                        stmt4.executeUpdate(sqldata);
                        String sqldata1 = "UPDATE usermineral " +
                                "SET redstone = redstone + 1 WHERE UUID in ('"+UUid+"')";
                        stmt5.executeUpdate(sqldata1);
                        p.sendMessage(ChatColor.GREEN + "redstone+1");
                        p.playSound(p.getLocation(), Sound.ENTITY_EXPERIENCE_ORB_PICKUP, 20, 1);
                        event.setCancelled(true);
                        block.setType(Material.AIR);

                    }
                    catch (SQLException ed) {
                        ed.printStackTrace();

                    }

                }
                x=0;
            }

        }
        catch (SQLException ed) {
            ed.printStackTrace();
        }

    }
}