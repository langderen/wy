package com.example.voting_back.controller;


import cn.dev33.satoken.annotation.SaCheckLogin;
import cn.dev33.satoken.annotation.SaIgnore;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.voting_back.common.Result;
import com.example.voting_back.entity.Options;
import com.example.voting_back.entity.Poll;

import com.example.voting_back.service.OptionsService;
import com.example.voting_back.service.PollService;
import com.example.voting_back.service.VotesService;
import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@SaCheckLogin
@RestController
@RequestMapping("/poll")
public class PollController {
    @Resource
    private PollService pollService ;

    /*
     * 创建新的投票活动
     * */

    @PostMapping
    public Result newPoll(@RequestBody Poll poll) {
        return Result.success(pollService.save(poll));
    }



    /*
     * 分页获取所有投票列表
     */
    @SaIgnore
    @GetMapping("/voteslist")
    public Result getVotesList(@RequestParam(defaultValue = "1")int pageNum ) {
        IPage<Poll> page = new Page<>(pageNum, 10);
        IPage<Poll> pollPage = pollService.page(page); // 调用 page 方法
        List<Poll> pollList = pollPage.getRecords();
        return Result.success(pollList);
    }
    /*
     * 通过创建者id获取创建者创建的活动
     * */

    @GetMapping("/getvote")
    public Result getVotesById(@RequestParam int creatorId ){
        Map<String, Object> columnMap = new HashMap<>();
        columnMap.put("creator_id", creatorId);
        Collection<Poll> polls = pollService.listByMap(columnMap);
        return Result.success(polls);
    }
    @DeleteMapping()
    public Result deletePoll(@RequestParam Long id){
        return Result.success(pollService.removeById(id));
    }

    /*
     * 修改活动信息*/
    @PutMapping
    public  Result updatePoll(@RequestBody Poll poll){

        return Result.success(pollService.updateById(poll));
    }
}
